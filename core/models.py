from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class History(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    action = models.CharField(max_length=16)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.timestamp) + ": " + str(self.user) + " " + self.action


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Compartment(models.Model):
    location = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self):
        return self.location


class Item(models.Model):
    name = models.CharField(max_length=32)
    location = models.ForeignKey(Compartment, on_delete=models.CASCADE)  # TODO on_delete = SET_NULL
    tags = models.ManyToManyField(Tag)
    state = models.BooleanField()
    history = models.ManyToManyField(History)

    def __str__(self):
        return self.name
