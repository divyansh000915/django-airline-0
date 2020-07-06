from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger #for using Flight object. .models means from models package of current package

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all() #the way django passes info to the templates (like jinja in flask) is through context dictionary, that maintains keys and values
    }
    return render(request, "flights/index.html", context)#naming the routes bcz can also refere to these routes via these names insted of /....

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist") #built in type of error in django
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all() #passing non passengers as well. The opposite of exclude function is filter()
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection."})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight."})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger."})
    passenger.flights.add(flight)#using this changes made correspondingly in in-between table as well
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))#syntax for routing using the name of the route, 
    #reverse("name of the route", args=(arguments accepted by new route))

