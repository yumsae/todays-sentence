from django.urls import path

# from profileapp.views import AccountDetailView
from profileapp import views

app_name = 'profileapp'

urlpatterns = [
    path('mypage/', views.MyPage, name='mypage'),
    path('profile/', views.profile_view, name='profile'),
    ]

