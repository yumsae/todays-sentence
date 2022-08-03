from django.urls import path
from django.contrib.auth import views as auth_views

from accountapp.views import AccountCreateView

app_name = 'accountapp'


urlpatterns = [
    path('create/', AccountCreateView.as_view(), name="create"),
    path('login/', auth_views.LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
