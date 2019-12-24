from django.db import models

# Create your models here.


class Match(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending"
        WIN = "win"
        LOSE = "lose"

    def __str__(self):
        return str(self.matchid)
    matchid = models.BigAutoField(primary_key=True)
    status = models.CharField(choices=Status.choices, default=Status.PENDING)
    score = models.BigIntegerField()
    playtime = models.DateTimeField()
    turn_count = models.IntegerField()
    spawned_alias = models.IntegerField()
    killed_alias = models.IntegerField()
    killed_hostiles = models.IntegerField()
    damage = models.IntegerField()
    heal = models.IntegerField()

