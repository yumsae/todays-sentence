from asyncore import write
from sqlite3 import Time
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
from buildapp.models import Article

def home(request):
    return render(request, 'buildapp/home.html')


def write_sentence(request):
    return render(request, 'buildapp/write_sentence.html')


def write_poet(request):
    # model = Article
    #
    # if request.method == 'POST':
    #
    #

    return render(request, 'buildapp/write_page.html')

@login_required(login_url='/account/login/')
def write_poet(request):

    # articles = Article.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title', False)
        text = request.POST.get('text', False)

        writer = request.user

        article = Article()
        article.title = title
        article.text = text
        article.writer = writer
        article.save()

        return render(request, 'profileapp/mypage.html')

    return render(request, 'buildapp/write_page.html')


def community(request):
    return render(request, 'buildapp/tst_write_community.html')

