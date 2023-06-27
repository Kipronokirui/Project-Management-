from django.shortcuts import render
from .serializers import Category, CategorySerializer, Post, PostSerializer, CreateUpdatePostSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import filters, generics, permissions, status, views
# from django.http.response import Http404, JsonResponse
from users.models import Profile

# Create your views here.
class CategoryAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDetailView(views.APIView):
    def get(self, request, slug):
        queryset = Category.objects.get(slug=slug)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)
    
    def put(self, request, slug):
        queryset = Category.objects.get(slug=slug)
        serializer = CategorySerializer(instance=queryset, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, slug):
        category_to_delete = Category.objects.get(slug=slug)
        delete_operation = category_to_delete.delete()
        data = {}
        if delete_operation:
            data["success"] = "Deletion was successful"
        else:
            data["failure"] = "Deletion failed"
        return Response(data=data)
    
class PostsListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class CreatePostAPIView(views.APIView):
    def post(self, request):
        current_user = User.objects.get(username="admin")
        author = Profile.objects.get(user=current_user)
        category = Category.objects.get(pk=1)
        data = request.data
        # data['author'] = author
        # data['category']= category
        serializer = CreateUpdatePostSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailView(views.APIView):
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
    
    def delete(self, request, slug):
        post_to_delete = Post.objects.get(slug=slug)
        delete_operation = post_to_delete.delete()
        data = {}
        if delete_operation:
            data["success"] = "Deletion was successful"
        else:
            data["failure"] = "Deletion failed"
        return Response(data=data)
