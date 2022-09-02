from asyncore import write
from sqlite3 import Time

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from buildapp.forms import SentenceCreationForm
from buildapp.models import Article, Sentence


def home(request):
    return render(request, 'buildapp/home.html')


@login_required(login_url='/accounts/login/')
def write_sentence(request): 
    if request.method == 'GET' :
        return render(request, 'buildapp/write_sentence.html')

    if request.method == 'POST' :
        list_sentence = request.POST.getlist('sentence[]') # 선택되지 않은 문장 가져오기 
        
        list_selected = request.POST.getlist('selectedSentence[]') # 선택된 문장 가져오기 

        writer = request.user
        return render('buildapp/write_page.html', {'list_selected':list_selected})


@login_required(login_url='/accounts/login/')
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


