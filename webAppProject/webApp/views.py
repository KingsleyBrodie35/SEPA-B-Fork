from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def mapView(request):
    return render(request, "map.html")

def addCustomerView(request):
    return render(request, "addCustomer.html")