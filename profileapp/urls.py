from django.urls import path

from profileapp.views import AccountDetailView

app_name = 'profileapp'

urlpatterns = [
    path('detail/', AccountDetailView.as_view(), name="detail"),
    # path('mypage/', views.Mypage, name='mypage'),
    ]

