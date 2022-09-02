from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
# from accountapp.views import AccountCreateView
from buildapp.views import community, home, write_poet, SentenceCreateView

app_name = 'buildapp'

urlpatterns = [
    path('', home, name='home'),
    path('sentence/write', SentenceCreateView.as_view(), name="write_sentence"),
    path('poet/write', write_poet, name="write_poet"),
    path('community', community, name="community"),
]