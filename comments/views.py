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
