from django.urls import path
from weather.views import index, weather

urlpatterns = [
    path("", index, name="home-page"),
    path("weather/<str:city>", weather, name="city-weather"),
]
