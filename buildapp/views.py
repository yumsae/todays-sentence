from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, 'buildapp/home.html')

def write_sentence(request):
    return render(request, 'buildapp/write_sentence.html')

def write_poet(request):
    return render(request, 'buildapp/write_poet.html')