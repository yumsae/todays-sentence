
from django.forms import ModelForm

from buildapp.models import Sentence




class SentenceCreationForm(ModelForm):
    class Meta:
        model = Sentence
        fields = ['text', 'writer']
