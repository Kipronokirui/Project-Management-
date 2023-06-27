from rest_framework import serializers
from .models import Comment

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        # depth = 1
        fields='__all__'