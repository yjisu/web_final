from django.urls import path
from. import views
urlpatterns= [
path('board/', views.board, name='board'),
path('board/post/<int:pk>/',views.post_edit,name='post_detail'),
path('board/post/new/',views.post_new,name='post_new'),
path('board/post/<int:pk>/edit/',views.post_edit,name='post_edit'),
path('',views.main,name='main')
]
