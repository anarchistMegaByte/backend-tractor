# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TripData', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripsinformation',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='tripsinformation',
            name='mileage',
        ),
        migrations.RemoveField(
            model_name='tripsinformation',
            name='start_time',
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='avgRpm',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='avgSpeed',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='depthDesired',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='fuelConsumed',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='gearRatio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='gearType',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='mileageForTheTrip',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='perAcreCost',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='slipForTheTripInPercentage',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='totalArea',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='totalAreaCovered',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='totalTripTime',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='tripEndTimeInMilliSecs',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='tripId',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tripsinformation',
            name='tripStartTimeInMilliSecs',
            field=models.BigIntegerField(null=True),
        ),
    ]
