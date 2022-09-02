from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
# from accountapp.views import AccountCreateView
from buildapp.views import community, home, write_poet

app_name = 'buildapp'

urlpatterns = [
    path('', home, name='home'),
    path('poet/write', write_poet, name="write_poet"),
    path('community', community, name="community"),
]