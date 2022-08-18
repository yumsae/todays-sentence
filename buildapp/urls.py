from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
# from accountapp.views import AccountCreateView
from buildapp.views import home, write_poet, write_sentence

app_name = 'buildapp'


urlpatterns = [
    path('', home, name='home'),
    path('sentence/write', write_sentence, name="write_sentence"),
    path('poet/write', write_poet, name="write_poet"),
]