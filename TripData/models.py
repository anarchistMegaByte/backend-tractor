from django.db import models

# Create your models here.
class TripsInformation(models.Model):
    mileage = models.IntegerField()
    start_time = models.DateField()
    end_time = models.DateField()
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
    