from django.urls import path

# from profileapp.views import AccountDetailView
from profileapp import views

app_name = 'profileapp'

urlpatterns = [
    path('mypage/', views.MyPage, name='mypage'),
<<<<<<< HEAD
    path('profile/', views.profile_view, name='profile'),
=======
    
>>>>>>> 2acbae3e833235bc67f3748f37f23476a4fec6ac
    ]

