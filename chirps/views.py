from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the chirps index.")

def edit(request, chirp_id):
    return HttpResponse("Hello, world. You're at the chirps edit index.")
