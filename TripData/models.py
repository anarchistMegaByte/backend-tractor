from django.db import models


# Create your models here.
class TripsInformation(models.Model):
   
    tripId = models.BigIntegerField(null=True);
    tripStartTimeInMilliSecs = models.BigIntegerField(null=True);
    tripEndTimeInMilliSecs = models.BigIntegerField(null=True);
    totalArea = models.BigIntegerField(null=True);
    totalAreaCovered = models.BigIntegerField(null=True);
    mileageForTheTrip = models.FloatField(null=True);
    depthDesired = models.FloatField(null=True);
    gearType = models.CharField(max_length=50, null=True);
    gearRatio = models.FloatField(null=True);
    fuelConsumed = models.FloatField(null=True);
    totalTripTime = models.FloatField(null=True);
    slipForTheTripInPercentage = models.FloatField(null=True);
    perAcreCost = models.FloatField(null=True);
    avgRpm = models.FloatField(null=True);
    avgSpeed = models.FloatField(null=True);
    
    def __str__(self):
        return u'%s' % (self.mileage)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    date_created = models.DateField()
    trips = models.ManyToManyField(TripsInformation)

    def __str__(self):
        return u'%s %s' % (self.email, self.trips)
    