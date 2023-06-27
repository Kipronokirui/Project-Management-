from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from users.models import Profile
from content.models import Post

# Create your models here.
class Comment(models.Model):
    commenter = models.ForeignKey(Profile, related_name='commenter', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    image = models.ImageField(upload_to='comments', blank=True, null=True)
    
    def __str__(self):
        return self.commenter.user.username