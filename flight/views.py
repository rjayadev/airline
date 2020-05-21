from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

from .models import Flight, Passenger

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"flight/login.html",{"message":None})
    context={
        #"user":request.user,
        "flights":Flight.objects.all()
    }
    return render(request,"flight/index.html",context)
def login(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        auth_login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"flight/login.html",{"message":"invalid credentials"})

def logout(request):
    auth_logout(request)
    return render(request,"flight/login.html",{"message":"Logged out"})

def flight(request,flight_id):
    if not request.user.is_authenticated:
        return render(request,"flight/login.html",{"message":None})
    try:
        flight=Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("No flight exist")
    context={
        "flight":flight,
        "passengers": flight.passenger_list.all(),
        "non_passengers":Passenger.objects.exclude(fights=flight).all()
    }
    return render(request,"flight/flight.html",context)

def book(request,flight_id):
    if not request.user.is_authenticated:
        return render(request,"flight/login.html",{"message":None})
    try:
        passenger_id=int(request.POST["passenger"])
        passenger=Passenger.objects.get(pk=passenger_id)
        flight=Flight.objects.get(pk=flight_id)
    except Passenger.DoesNotExist:
        return render(request,"flight/error.html",{"message":"Invalid passenger id"})
    except Flight.DoesNotExist:
        return render(request,"flight/error.html",{"message":"Invalid flight id"})
    except KeyError:
        return render(request,"flight/error.html",{"message":"invalid selection"})
    passenger.fights.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(flight.id,)))
