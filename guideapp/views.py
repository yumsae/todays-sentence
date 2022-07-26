from django.shortcuts import render

def guideMain(request):
    return render(request,'guide_page.html')