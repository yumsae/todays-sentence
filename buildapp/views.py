from django.shortcuts import render

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





def community(request):
    return render(request, 'buildapp/tst_write_community.html')

