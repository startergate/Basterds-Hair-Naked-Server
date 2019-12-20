import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseForbidden

from auth_sid.models import User
from .forms import UserForm

# Create your views here.


def index(request):
    return HttpResponseForbidden()


def login_handler(request):
    return HttpResponseRedirect(redirect_to="")


def session(request):
    if request.method != "POST":
        return HttpResponse(status=500)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    res = requests.post('http://sid.donote.co:3000/api/v1/session/', {
        "type": "login",
        "clientid": body["clientid"],
        "userid": body["id"],
        "password": body["pw"],
        "isPermanent": True,
    }).json()
    if res["type"] == "error":
        return HttpResponse(status=500)
    fakepost = {
        'id': body['id'],
        'pid': res["response_data"][0]
    }
    user = User(id=body["id"], pid=res["response_data"][1])
    form = UserForm(fakepost, instance=user)
    if form.is_valid():
        form.save()
        return JsonResponse({
            "sessid": res["response_data"][0],
            "pid": res["response_data"][1],
            "nickname": res["response_data"][2]
        })
    else:
        return HttpResponse(status=500)
