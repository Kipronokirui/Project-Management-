from django.shortcuts import render
from .serializers import Category, CategorySerializer, Post, PostSerializer, CreateUpdatePostSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import filters, generics, permissions, status, views
from django.http.response import Http404, JsonResponse

# Create your views here.
class CategoryAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDetailView(views.APIView):
    def get(self, request, slug):
        queryset = Category.objects.get(slug=slug)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)
    
class PostsListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class PostDetailView(views.APIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request, slug):
        queryset = Post.objects.get(slug=slug)
        serializer = PostSerializer(queryset, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        queryset = Post.objects.get(slug=slug)
        serializer = CreateUpdatePostSerializer(instance=queryset, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
