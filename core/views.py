from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from core.models import Location


def index(request):
    return render(request=request, template_name='core/index.html', context={"locations": Location.objects.all})
