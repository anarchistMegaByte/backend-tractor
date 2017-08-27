from django.shortcuts import render
from TripData.models import TripsInformation
from django.http import Http404, HttpResponse

# Create your views here.
def check_query(request):
    trip_list = TripsInformation.objects.all()
    output = ""
    for trips in trip_list:
        output = output + "-" + str(trips.mileage)
    
    return HttpResponse(output)

    