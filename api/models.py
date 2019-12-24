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
    pid = models.ForeignKey(User, db_column="pid", help_text="유저 테이블 외래키", on_delete=models.CASCADE)
    played_as = models.CharField(max_length=12, choices=Faction.choices, default=Faction.INSOMNIA)
    status = models.CharField(max_length=7, choices=Status.choices, default=Status.PENDING)
    score = models.BigIntegerField()
    playtime = models.DateTimeField()
    turn_count = models.IntegerField()
    spawned_alias = models.IntegerField()
    killed_alias = models.IntegerField()
    killed_hostiles = models.IntegerField()
    damage = models.IntegerField()
    heal = models.IntegerField()

