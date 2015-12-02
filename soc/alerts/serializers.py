from rest_framework import serializers
from models import *

class AfflictionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Affliction
		fields = ('user', 'disease')
		
class DiseaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Disease
		fields = ('disease', 'aqi', 'pm', 'ozone')
