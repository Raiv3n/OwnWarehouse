from django.contrib import admin
from .models import Item, History, Location, Tag

# Register your models here.
admin.site.register(Item)
admin.site.register(History)
admin.site.register(Location)
admin.site.register(Tag)
