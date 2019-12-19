from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden

# Create your views here.


def index(request):
    return HttpResponseForbidden()


def login_handler(request):
    return HttpResponseRedirect(redirect_to="")
