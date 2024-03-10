from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    return render(request, "core/index.html", {
        'users': User.objects.all()
    })
