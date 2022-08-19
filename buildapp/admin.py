from django.contrib import admin

# Register your models here.
from buildapp.models import Sentence, Article

admin.site.register(Sentence)
admin.site.register(Article)