from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin


from profileapp.forms import ProfileCreationForm


#def Create(request):
#    if request.method == 'GET':
#        return render(request, 'profileapp/create.html')
# def Create(request):
#     if request.method == "POST":
#         form = ProfileCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             nickname = form.cleaned_data.get('nickname')
#             return redirect('buildapp:home')
#     else:
#         form = ProfileCreationForm()
#     return render(request, 'profileapp/create.html', {'form': form})
#
#
# class Nickname:
#     pass


def Create(request):

    if request.method == 'POST':
        Nickname = request.POST.get('nickname', False)


        nickname = Nickname()

        nickname.save()

        return render(request, 'buildapp:home')

    return render(request, 'profileapp/create.html')



from profileapp.models import Profile




def MyPage(request):
    return render(request, 'profileapp/mypage.html')


def ProfileCreate(request):
    if request.method == 'POST':

        profile = Profile()
        profile.user = request.user
        profile.nickname = request.POST['nickname']
        profile.message = request.POST['message']
        profile.save()













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

        return redirect('buildapp:home')
    return render(request, 'profileapp/create.html')

