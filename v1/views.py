from datetime import datetime, timedelta

from django.core import serializers
from django.http import HttpResponse, JsonResponse

import json

from api.models import Match

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def get_profile(request, pid):
    default_time = datetime.min
    base = {
        "pid": pid,
        "total": {
            "avg_score": 0,
            "score": 0,
            "playtime": default_time,
            "most_played": "insomnia",
            "best_played": "insomnia",
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "pending_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "insomnia": {
            "score": 0,
            "playtime": default_time,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "pending_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "orangefamily": {
            "score": 0,
            "playtime": default_time,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "pending_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "overhit": {
            "score": 0,
            "playtime": default_time,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "pending_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        },
        "meisterboi": {
            "score": 0,
            "playtime": default_time,
            "turn_count": 0,
            "match_count": 0,
            "win_count": 0,
            "pending_count": 0,
            "spawned": 0,
            "killed": 0,
            "damage": 0
        }
    }
    result = Match.objects.filter(player=pid)
    for i, d in enumerate(result):
        base[d.played_as]["score"] += d.score
        base[d.played_as]["playtime"] += timedelta(hours=d.playtime.hour, minutes=d.playtime.minute,
                                                   seconds=d.playtime.second, microseconds=d.playtime.microsecond)
        base[d.played_as]["turn_count"] += d.score
        base[d.played_as]["match_count"] += 1
        base[d.played_as]["win_count"] += 1 if d.status == d.Status.WIN else 0
        base[d.played_as]["pending_count"] += 1 if d.status == d.Status.PENDING else 0
        base[d.played_as]["spawned"] += d.spawned
        base[d.played_as]["killed"] += d.killed
        base[d.played_as]["damage"] += d.score

        base["total"]["score"] += d.score
        base["total"]["playtime"] += timedelta(hours=d.playtime.hour, minutes=d.playtime.minute,
                                               seconds=d.playtime.second, microseconds=d.playtime.microsecond)
        base["total"]["turn_count"] += d.score
        base["total"]["match_count"] += 1
        base["total"]["win_count"] += 1 if d.status == d.Status.WIN else 0
        base["total"]["pending_count"] += 1 if d.status == d.Status.PENDING else 0
        base["total"]["spawned"] += d.spawned
        base["total"]["killed"] += d.killed
        base["total"]["damage"] += d.score

    try:
        base["total"]["avg_score"] = base["total"]["score"] / base["total"]["match_count"]
    except ZeroDivisionError:
        pass

    playtime_top = datetime.min
    count_per_match_top = 0
    for key, value in base.items():
        if key not in ["insomnia", "orangefamily", "overhit", "meisterboi"]:
            continue
        if playtime_top < value["playtime"]:
            base["total"]["most_played"] = key
        try:
            if count_per_match_top < value["score"] / value["match_count"]:
                base["total"]["best_played"] = key
        except ZeroDivisionError:
            pass

    return JsonResponse(base)


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
