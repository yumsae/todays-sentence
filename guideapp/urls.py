from django.urls import path
import guideapp.views
from django.contrib.auth import views as auth_views

app_name = 'guideapp'




urlpatterns = [
    path('guide/', guideapp.views.guideMain, name="guideMain"),

]