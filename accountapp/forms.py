from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(label="닉네임")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nickname')
