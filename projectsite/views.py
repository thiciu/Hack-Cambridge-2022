from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


def index(request):
    return render(request,"test.html")