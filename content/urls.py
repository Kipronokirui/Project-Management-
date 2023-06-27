from django.urls import path
from .views import CategoryAPIView, PostsListAPIView, CategoryDetailView, PostDetailView

urlpatterns=[
    path('categorys/', CategoryAPIView.as_view()),
    path('category/<str:slug>/', CategoryDetailView.as_view()),
    path('posts/', PostsListAPIView.as_view()),
    path('post/<str:slug>/', PostDetailView.as_view()),
    path('post/<str:slug>/update/', PostDetailView.as_view()),
]