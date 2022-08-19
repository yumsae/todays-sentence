from django.forms import ModelForm

from buildapp.models import Sentence, Article


class SentenceCreationForm(ModelForm):
    class Meta:
        model = Sentence
        fields = ['text', 'writer']



class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

