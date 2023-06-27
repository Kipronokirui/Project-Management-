from django.shortcuts import render
from .serializers import Comment, CommentsSerializer
from content.models import Post
from users.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import filters, generics, permissions, status, views

# Create your views here.
class CommentsView(APIView):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        post=post.pk
        data = request.data
        data['post'] = post
        serializer=CommentsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentsSerializer(instance=queryset, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment_to_delete = Comment.objects.get(pk=pk)
        delete_operation = comment_to_delete.delete()
        data = {}
        if delete_operation:
            data["success"] = "Deletion was successful"
        else:
            data["failure"] = "Deletion failed"
        return Response(data=data)
