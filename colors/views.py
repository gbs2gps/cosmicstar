from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'colors/colorstuff.html')

# Create your views here.
