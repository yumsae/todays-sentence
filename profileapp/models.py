from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)




#class Article(models.Model):
#    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
#    info = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='article', null=True)
#
#    title = models.CharField(max_length=100, null=True)
#    text = models.TextField(null=False)
#    created_at = models.DateTimeField(auto_now=True)