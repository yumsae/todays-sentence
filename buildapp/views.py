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


@method_decorator(login_required, name='dispatch')
class SentenceCreateView(CreateView):
    model = Sentence
    form_class = SentenceCreationForm
    template_name = 'buildapp/write_sentence.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.writer = self.request.writer
        temp_comment.save()

        self.list_sentence = self.request.POST.getlist('sentence-select') # 선택된 문장 가져오기 

        return super().form_valid(form)

    def get_success_url(self) :
        return super().get_success_url() # context + render 필요 



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

