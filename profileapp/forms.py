from django.forms import ModelForm

from accountapp import forms
from profileapp.models import Profile
from django.contrib.auth.forms import UserChangeForm

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

#class CustomCsUserChangeForm(UserChangeForm):
#    password = None
#    hp = forms.IntegerField(label='', widget=forms.NumberInput(
#        attrs={'class': 'form-control', 'maxlength': '11', 'oninput': "maxLengthCheck(this)", }),
#    )
