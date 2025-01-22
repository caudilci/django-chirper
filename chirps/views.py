from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Chirp

# Create your views here.

def index(request):
    latest_chirp_list = Chirp.objects.order_by("-created_at")
    template = loader.get_template("index.html")
    context = {
        "latest_chirp_list": latest_chirp_list,
    }
    return HttpResponse(template.render(context, request))

def edit(request, chirp_id):
    return HttpResponse("Hello, world. You're at the chirps edit index.")
