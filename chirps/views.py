from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Chirp

# Create your views here.

def index(request):
    latest_chirp_list = Chirp.objects.order_by("-created_at")
    context = {
        "latest_chirp_list": latest_chirp_list,
    }
    return render(request, "index.html", context)

def edit(request, chirp_id):
    try:
        chirp = Chirp.objects.get(pk=chirp_id)
    except Chirp.DoesNotExist:
        raise Http404("Chirp does not exist")
    return HttpResponse(f'Hello, world. Edit message "{chirp.message}" ')
