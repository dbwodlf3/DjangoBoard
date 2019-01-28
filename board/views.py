from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def views1(request):
    return render(request, "board/index.html")