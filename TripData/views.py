from django.shortcuts import render
from TripData.models import TripsInformation
from django.http import Http404, HttpResponse
import datetime,json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def check_query(request):
    trip_list = TripsInformation.objects.all()
    output = ""
    for trips in trip_list:
        output = output + "-" + str(trips.tripId)
    
    return HttpResponse(output)

def insert_query(request):
    t1 = TripsInformation()
    t1.mileage = 16
    t1.start_time = datetime.datetime.now()
    t1.end_time = datetime.datetime.now()
    t1.save()
    output = "inserted"
    
    return HttpResponse(output)

@csrf_exempt 
def sample_upload_request(request):
    json_data = json.loads(request.body.decode(encoding='UTF-8'))
    #print('Raw Data : %s' % json_data)
    first_level_keys = []
    for key in json_data.keys():
        first_level_keys.append(key)
        print("Key: %s" % key)

    tripInfo = TripsInformation()
    tripInfo.tripId = json_data['tripId']
    tripInfo.tripStartTimeInMilliSecs = json_data['tripStartTimeInMilliSecs']
    tripInfo.tripEndTimeInMilliSecs = json_data['tripEndTimeInMilliSecs']
    tripInfo.totalArea = json_data['totalArea']
    tripInfo.totalAreaCovered = json_data['totalAreaCovered']
    tripInfo.mileageForTheTrip = json_data['mileageForTheTrip']
    tripInfo.depthDesired = json_data['depthDesired']
    tripInfo.gearType = json_data['gearType']
    tripInfo.gearRatio = json_data['gearRatio']
    tripInfo.fuelConsumed = json_data['fuelConsumed']
    tripInfo.totalTripTime = json_data['totalTripTime']
    tripInfo.slipForTheTripInPercentage = json_data['slipForTheTripInPercentage']
    tripInfo.perAcreCost = json_data['perAcreCost']
    tripInfo.avgRpm = json_data['avgRpm']
    tripInfo.avgSpeed = json_data['avgSpeed']
    tripInfo.save()

    print("Length of keys %d " % len(first_level_keys))

    print(len(json_data['gpsPoints']))

    for tempo in json_data['gpsPoints']:
        print(tempo['rpmCounter'])

    return HttpResponse("Done : %d " % tripInfo.tripId)