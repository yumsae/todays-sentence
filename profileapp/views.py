from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

#from profileapp.forms import CustomCsUserChangeForm
#from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm


#def Create(request):
#    if request.method == 'GET':
#        return render(request, 'profileapp/create.html')
def Create(request):
    if request.method == "POST":
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data.get('nickname')
            return redirect('profileapp:create')
    else:
        form = ProfileCreationForm()
    return render(request, 'buildapp:home', {'form': form})
#    return render(request, 'profileapp/create.html', {'form': form})
#def Create(request):
#    if request.method == "POST":
#        form = ProfileCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=raw_password)  # 사용자 인증
#            login(request, user)  # 로그인
#            return redirect('profileapp:create')  # 바꿔야
#    else:
#        form = UserForm()
#    return render(request, 'accountapp/create.html', {'form': form})








def MyPage(request):
    return render(request, 'profileapp/mypage.html')

# users/views.py

def View(request):
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


