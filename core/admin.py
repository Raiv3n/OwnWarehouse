from django.contrib import admin
from .models import Item, History, Compartment, Tag
# Register your models here.
admin.site.register(Item)
admin.site.register(History)
admin.site.register(Compartment)
admin.site.register(Tag)