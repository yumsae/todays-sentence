from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'password1', 'password2', 'email')
=======
        fields = ('username', 'password1', 'password2', 'email', )
>>>>>>> 5761a691381827596f0298e139d51d75a4edb637
