from django.core import serializers
from django.http import HttpResponse, JsonResponse

import json

from api.models import Match

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def get_profile(request, pid):
    return JsonResponse({
        "pid": pid,
        "total": {
            "score": 0,
            "playtime": 0,
            "most_played": "meisterboi",
            "best_played": "meisterboi",
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "insomnia": {
            "score": 0,
            "playtime": 0,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "orangefamily": {
            "score": 0,
            "playtime": 0,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "overhit": {
            "score": 0,
            "playtime": 0,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "meisterboi": {
            "score": 0,
            "playtime": 0,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        }
    })


def get_matches(request, pid):
    match_list = json.loads(serializers.serialize('json', Match.objects.filter(player=pid)))
    match_list = [x["fields"] for x in match_list]
    return JsonResponse({
        "is_succeed": True,
        "data": match_list
    })


def get_match_specific(request, match_id):
    return JsonResponse({
        "is_succeed": True,
        "data": json.loads(serializers.serialize('json', Match.objects.filter(matchid=match_id)))[0]["fields"]
    })
