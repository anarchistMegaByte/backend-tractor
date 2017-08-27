from django.shortcuts import render
from TripData.models import TripsInformation
from django.http import Http404, HttpResponse
import datetime

# Create your views here.
def check_query(request):
    trip_list = TripsInformation.objects.all()
    output = ""
    for trips in trip_list:
        output = output + "-" + str(trips.mileage)
    
    return HttpResponse(output)

def insert_query(request):
    t1 = TripsInformation()
    t1.mileage = 16
    t1.start_time = datetime.datetime.now()
    t1.end_time = datetime.datetime.now()
    t1.save()
    output = "inserted"
    
    return HttpResponse(output)