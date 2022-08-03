from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountCreateView
from buildapp.views import home

app_name = 'buildapp'


urlpatterns = [
    path('', home, name='home')
    ]