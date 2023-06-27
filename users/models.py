from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    about_me = models.TextField(verbose_name=_("About Me"), default="Say something about yourself")
    
    def __str__(self):
        return self.user.username
