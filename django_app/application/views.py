from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def page1(request):
    return render(request, 'home/page1.html')

def page2(request):
    return render(request, 'home/page2.html')

def page3(request):
    return render(request, 'home/page3.html')

def page4(request):
    return render(request, 'home/page4.html')