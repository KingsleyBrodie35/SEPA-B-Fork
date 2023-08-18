from django.urls import path
from . import views

#routes for our views functions
urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.map_view, name="map")
]