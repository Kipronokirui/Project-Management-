from django.shortcuts import render
from rest_framework import views, generics
from .serializers import Category, CategorySerializer, Post, PostSerializer

# Create your views here.
class CategoryAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PostsListAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()