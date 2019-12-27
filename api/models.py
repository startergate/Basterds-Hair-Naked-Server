from datetime import datetime

from django.db import models

from auth_sid.models import User

# Create your models here.


class Faction(models.TextChoices):
    INSOMNIA = "insomnia"
    ORANGEFAMILY = "orangefamily"
    OVERHIT = "overhit"
    MEISTERBOI = "meisterboi"


class Match(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending"
        WIN = "win"
        LOSE = "lose"

    def __str__(self):
        return str(self.matchid)

    matchid = models.BigAutoField(primary_key=True)
    player1 = models.ForeignKey(User, db_column="player1", help_text="유저 테이블 외래키", on_delete=models.CASCADE, related_name="pid1", null=True)
    player2 = models.ForeignKey(User, db_column="player2", help_text="유저 테이블 외래키", on_delete=models.CASCADE, related_name="pid2", null=True)
    played_as1 = models.CharField(max_length=12, choices=Faction.choices, default=Faction.INSOMNIA)
    played_as2 = models.CharField(max_length=12, choices=Faction.choices, default=Faction.INSOMNIA)
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.PENDING)
    score1 = models.BigIntegerField()
    score2 = models.BigIntegerField()
    playtime = models.DateTimeField()
    turn_count = models.IntegerField()
    spawned1 = models.IntegerField()
    killed1 = models.IntegerField()
    spawned2 = models.IntegerField()
    killed2 = models.IntegerField()
    damage1 = models.BigIntegerField()
    heal1 = models.BigIntegerField()
    damage2 = models.BigIntegerField()
    heal2 = models.BigIntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    terminated_at = models.DateTimeField(null=True)


class Object(models.Model):
    class Status(models.TextChoices):
        UNBORN = "unborn"
        ALIVE = "alive"
        STUN = "stun"
        DEAD = "dead"
        DONE = "done"

    class Job(models.TextChoices):
        LEADER = "leader"
        BASIC = "basic"
        ADVANCED = "advanced"
        EXPERT = "expert"

    objectid = models.BigAutoField(primary_key=True)
    matchid = models.ForeignKey(Match, db_column="matchid", help_text="매치 테이블 외래키", on_delete=models.CASCADE)
    belong_to = models.ForeignKey(User, db_column="pid", help_text="유저 테이블 외래키", on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.UNBORN)
    faction = models.CharField(max_length=12, choices=Faction.choices, default=Faction.INSOMNIA)
    job = models.CharField(max_length=8, choices=Job.choices, default=Job.LEADER)
    hp = models.IntegerField()
    damage = models.IntegerField()


class Action(models.Model):
    class ActionType(models.TextChoices):
        SPAWN = "spawn"
        MOVE = "move"
        ATTACK = "attack"
        MOVEATTACK = "moveattack"
        DIE = "die"

    def __str__(self):
        return "some string"

    actionid = models.BigAutoField(primary_key=True)
    pid = models.ForeignKey(User, db_column="pid", help_text="유저 테이블 외래키", on_delete=models.CASCADE)
    matchid = models.ForeignKey(Match, db_column="matchid", help_text="매치 테이블 외래키", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ActionType.choices, default=ActionType.MOVE)
    origin = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='action_origin')
    to = models.ForeignKey(Object, on_delete=models.CASCADE, null=True, related_name='action_to')
    destination_x = models.IntegerField(null=True)
    destination_y = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
