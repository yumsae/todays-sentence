from django.urls import path


from profileapp import views

app_name = 'profileapp'

urlpatterns = [
    path('mypage/', views.MyPage, name='mypage'),
    path('create/', views.ProfileCreate, name='create'),
]

