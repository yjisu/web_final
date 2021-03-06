from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.shortcuts import render,get_object_or_404
from .forms import PostForm , CommentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    all_boards = Post.objects.all().order_by("-created_date")
    page = int(request.GET.get('p',1))
    pagenator = Paginator(all_boards,2)
    posts = pagenator.get_page(page)
    return render(request, 'blog/blog.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def main(request):
    return render(request, 'blog/main.html')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
