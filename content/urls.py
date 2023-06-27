from django.urls import path
from .views import CategoryAPIView, PostsListAPIView

urlpatterns=[
    path('categorys/', CategoryAPIView.as_view()),
    path('posts/', PostsListAPIView.as_view())
]