from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from profileapp.models import Profile


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    info = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=100, null=True)
    text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)

class Sentence(models.Model):
    text = models.TextField(null=True)