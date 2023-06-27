from rest_framework import serializers
from .models import Category, Post
from users.serializers import ProfileSerializer

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'slug', 'category_id']
        
    
class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only = True )
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'slug', 'post_id', 'category', 'author']
    
class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'slug', 'category_id', 'posts']
        
    def get_posts(self, obj):
        serializer = PostSerializer(obj.posts.all(), many = True)
        return serializer.data
        