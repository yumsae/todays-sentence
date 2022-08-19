from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

#from profileapp.forms import CustomCsUserChangeForm
#from profileapp.models import Profile



def MyPage(request):
    return render(request, 'profileapp/mypage.html')

# users/views.py

def profile_view(request):
    if request.method == 'GET':
        return render(request, 'profileapp/profile.html')

#def profile_update_view(request):
#    if request.method == 'POST':
#        user_change_form = CustomCsUserChangeForm(request.POST, instance = request.user)
#
#        if user_change_form.is_valid():
#            user_change_form.save()
#            return render(request, 'users/profile.html')
#    else:
#        user_change_form = CustomCsUserChangeForm(instance = request.user)
#
#        return render(request, 'users/profile_update.html', {'user_change_form':user_change_form})

