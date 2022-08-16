from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

from profileapp.models import Profile



def MyPage(request):
    return render(request, 'profileapp/mypage.html')