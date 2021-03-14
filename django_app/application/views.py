from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from .forms import ResumeForm

def index(request):
    return render(request, 'home/index.html')

def page1(request):
    return render(request, 'home/page1.html')

def page2(request):
    return render(request, 'home/page2.html')

def page3(request):
    return render(request, 'home/page3.html')

def candidature(request):

    if request.method == "POST":
        form = ResumeForm(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')
    
    else:
        form = ResumeForm()

    return render(request, 'home/candidature.html', {'form':form})