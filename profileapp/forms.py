from django.forms import ModelForm


from accountapp import forms
from profileapp.models import Profile
from django.contrib.auth.forms import UserChangeForm

class ProfileCreationForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

