import time

from django.db import models


# Create your models here.
class Store(models.Model):
    STATE = (
        ('not_active', 0),
        ('active', 1)
    )
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    state = models.CharField(choices=STATE, max_length=10, default=1)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
