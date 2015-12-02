from django.db import models
from django.contrib import admin

class PollutantionData(models.Model):
	name = models.CharField(max_length=5)
	date = models.DateField()
	DAILY_AQI_VALUE = models.IntegerField(max_length=2)
	COUNTY_CODE = models.IntegerField(max_length=2)
	COUNTY = models.IntegerField(max_length=2)
	SITE_LATITUDE = models.FloatField(max_length=5)
	SITE_LONGITUDE = models.FloatField(max_length=5)
	
class Affliction(models.Model):
	user = models.CharField(max_length=30)
	disease = models.CharField(max_length=30)
	class Meta:
		unique_together = (('user', 'disease'))
	
class Disease(models.Model):
	disease = models.CharField(max_length=30, primary_key=True)
	aqi = models.IntegerField(max_length=3)
	pm = models.FloatField(max_length=5)
	ozone = models.FloatField(max_length=5)
	
admin.site.register(Affliction)
admin.site.register(Disease)
