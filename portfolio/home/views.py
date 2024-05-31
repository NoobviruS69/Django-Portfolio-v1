from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request , 'home/index.html')

def portfolio(request):
    return render(request , 'home/portfolio-details.html')