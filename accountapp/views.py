from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

from accountapp.forms import UserForm


# Create your views here.
from profileapp.models import Profile


def AccountCreate(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('profileapp:create')  # 바꿔야
    else:
        form = UserForm()
    return render(request, 'accountapp/create.html', {'form': form})



class AccountDetailView(DetailView, MultipleObjectMixin):
    model = Profile
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


