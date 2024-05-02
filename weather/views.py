from django.shortcuts import render

from weather.models import City, DailyWeather


def index(request):
    context = {"cities": City.objects.all()}
    return render(request, "home.html", context)


def weather(request, city):
    city_name = f"{city.title().replace('-', ' ')}"
    city_query = City.objects.get(name=city_name)
    city_weathers = DailyWeather.objects.filter(city=city_query)

    context = {"weathers": city_weathers}
    return render(request, "city_weather.html", context)
