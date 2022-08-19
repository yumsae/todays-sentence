from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

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

    # def input_test(request):
    #     if request.method == 'POST':
    #         list_sentence = request.POST.getlist('sentence-select')
    #
    #         for i in list_sentence:
    #             writer = request.user
    #             sentence = Sentence()
    #             sentence.text = i
    #             sentence.writer = writer
    #             sentence.save()





    # def form_valid(self, form):
    #     temp_comment = form.save(commit=False)
    #     temp_comment.article = Sentence.objects.get(pk=self.request.POST['sentence_pk'])
    #     temp_comment.writer = self.request.writer
    #     temp_comment.save()
    #     return super().form_valid(form)



@login_required(login_url='/account/login/')
def write_poet(request):

    # articles = Article.objects.all()

    def sentenceInsert(request):
        list_sentence = request.POST.getlist('sentence-select')
        return HttpResponse(request, 'buildapp/write_page.html', {'sentence':list_sentence})


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

