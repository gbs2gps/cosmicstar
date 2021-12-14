from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'colors/colorstuff.html')

def index1(request):
    return render(request, 'colors/colorstuff1.html')

def index2(request):
    return render(request, 'colors/colorstuff2.html')

def index3(request):
    return render(request, 'colors/colorstuff3.html')

def index4(request):
    return render(request, 'colors/colorstuff4.html')

def index5(request):
    return render(request, 'colors/colorstuff5.html')

def index6(request):
    return render(request, 'colors/colorstuff6.html')

def index7(request):
    return render(request, 'colors/colorstuff7.html')

def index8(request):
    return render(request, 'colors/colorstuff8.html')

# Create your views here.
