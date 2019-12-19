from django.db import models

# Create your models here.


class User(models.Model):
    def __str__(self):
        return self.id
    id = models.CharField(max_length=20, null=False, unique=True)
    uid = models.CharField(max_length=64, primary_key=True)
