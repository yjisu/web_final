from django.urls import path
from django.conf.urls import url
from. import views
urlpatterns= [
path('blog/', views.blog, name='blog'),
path('post/<int:pk>/',views.post_detail,name='post_detail'),
path('post/new/',views.post_new,name='post_new'),
path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
path('',views.main,name='main'),
]
