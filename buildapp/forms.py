<<<<<<< HEAD

from django.forms import ModelForm

from buildapp.models import Sentence




class SentenceCreationForm(ModelForm):
    class Meta:
        model = Sentence
        fields = ['text', 'writer']
=======
from dataclasses import field
from django.forms import ModelForm
from buildapp.models import Article

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
>>>>>>> 07c13ec744692792fe17a0d883af27a0113a4fd6
