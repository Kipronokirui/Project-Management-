from django.urls import path
from .views import CategoryAPIView, PostsListAPIView, CategoryDetailView, PostDetailView, CreatePostAPIView

urlpatterns=[
    path('categorys/', CategoryAPIView.as_view()),
    path('category/<str:slug>/', CategoryDetailView.as_view()),
    path('category/<str:slug>/update/', CategoryDetailView.as_view()),
    path('category/<str:slug>/delete/', CategoryDetailView.as_view()),
    path('posts/', PostsListAPIView.as_view()),
    path('posts/add-post/', CreatePostAPIView.as_view()),
    path('post/<str:slug>/', PostDetailView.as_view()),
    path('post/<str:slug>/update/', PostDetailView.as_view()),
    path('post/<str:slug>/delete/', PostDetailView.as_view()),
]