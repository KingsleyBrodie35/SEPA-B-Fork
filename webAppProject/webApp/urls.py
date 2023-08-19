from django.urls import path
from . import views

#routes for our views functions
urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.mapView, name="map"),
    path("addCustomer/", views.addCustomerView, name="addCustomer")
]