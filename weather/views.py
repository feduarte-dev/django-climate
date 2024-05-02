from django.shortcuts import render

from weather.models import City


def index(request):
    context = {"cities": City.objects.all()}
    return render(request, "home.html", context)
