from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.


def index(request):
    return HttpResponseForbidden()
