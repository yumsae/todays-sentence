from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accountapp.forms import UserForm


# Create your views here.


def AccountCreate(request):
    if request.method == "POST":
        # form = UserForm(request.POST)
        # if form.is_valid():
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('/')

    return render(request, 'accountapp/create.html')
