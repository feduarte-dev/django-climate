from django.shortcuts import render

from weather.models import City, DailyWeather
from datetime import date


def index(request):
    context = {"cities": City.objects.all()}
    return render(request, "home.html", context)


def weather(request, city):
    city_name = f"{city.title().replace('-', ' ')}"
    city_query = City.objects.get(name=city_name)
    city_weathers = DailyWeather.objects.filter(city=city_query)

    context = {"weathers": city_weathers}
    return render(request, "city_weather.html", context)


def weather_details(request, city, target):
    city_name = f"{city.title().replace('-', ' ')}"
    city_query = City.objects.get(name=city_name)
    weather_date = date.fromisoformat(target)

    city_weathers = DailyWeather.objects.get(
        city=city_query, date=weather_date
    )

    context = {"weather": city_weathers}
    return render(request, "weather_details.html", context)
