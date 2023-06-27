from django.db import models
import uuid
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from users.models import Profile

# Create your models here. 
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    category_id = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Profile, related_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    post_id = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return self.title
