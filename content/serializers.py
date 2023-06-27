from rest_framework import serializers
from .models import Category, Post
from users.serializers import ProfileSerializer
from comments.serializers import CommentsSerializer

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'slug', 'category_id']
        
    
class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only = True )
    category = PostCategorySerializer(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'slug', 'post_id', 'category', 'author','comments']
        
    def get_comments(self, obj):
        comments = obj.post_comment.all()
        serializer = CommentsSerializer(comments, many=True)
        return serializer.data

class CreateUpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'author']
        
class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'slug', 'category_id', 'posts']
        
    def get_posts(self, obj):
        serializer = PostSerializer(obj.posts.all(), many = True)
        return serializer.data
    
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description', 'image']
        