from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile



def MyPage(request):
    return render(request, 'profileapp/mypage.html')


# def Create(request):
#
#     if request.method == 'POST':
#         Nickname = request.POST.get('nickname', False)
#
#         nickname = Nickname()
#         nickname.save()
#
#         return render(request, 'buildapp:home')
#
#     return render(request, 'profileapp/create.html')



def ProfileCreate(request):
    if request.method == 'POST':

        profile = Profile()
        profile.user = request.user
        profile.nickname = request.POST['nickname']
        profile.message = request.POST['message']
        profile.save()

        return redirect('buildapp:home')
    return render(request, 'profileapp/create.html')