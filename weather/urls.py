from django.urls import path
from weather.views import index, weather, weather_details

urlpatterns = [
    path("", index, name="home-page"),
    path("weather/<str:city>", weather, name="city-weather"),
    path(
        "weather/<str:city>/<str:target>",
        weather_details,
        name="weather-details",
    ),
]
