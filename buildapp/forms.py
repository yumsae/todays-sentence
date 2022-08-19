from dataclasses import field
from django.forms import ModelForm
from buildapp.models import Article

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']