from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class History(models.Model):
    ADD = 'ADD'
    DELETE = "DEL"
    UPDATE = "UPD"
    STORE = "STR"
    OUT = "OUT"

    CHOICES = [
        (ADD, 'Add'),
        (DELETE, 'Delete'),
        (UPDATE, 'Update'),
        (STORE, 'Store'),
        (OUT, 'Out')
    ]

    user = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=3, choices=CHOICES, default=ADD)
    timestamp = models.DateTimeField(auto_now=True)

    @classmethod
    def get_new(cls):
        #pass
        return cls.objects.create().id

    def __str__(self):
        return str(self.timestamp) + ": " + str(self.user) + " " + self.action


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash((self.name, self.name))

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self == other


class Location(models.Model):
    location = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self):
        return self.location

    def get_tags(self):
        tags = {}
        for item in Item.objects.all():
            for tag in item.tags:
                if tag in tags:
                    tags[item] = tag[item] + 1
                else:
                    tags[item] = 1


class Item(models.Model):
    name = models.CharField(max_length=32)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  # TODO on_delete = SET_NULL
    tags = models.ManyToManyField(Tag)
    state = models.BooleanField()
    history = models.ManyToManyField(History, default=History.get_new())

    def __str__(self):
        return self.name
