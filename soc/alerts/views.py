from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from forms import *
from django.contrib.auth.models import User
from urllib2 import urlopen
from json import load, dumps

global alert
alert = ""

def home(request):
	if request.method == 'GET':
		return render(request, "home.html", {'form':LoginForm()})
	elif request.method == 'POST':
		u = User.objects.get(username=request.POST['username'])
		if u.password == request.POST['password']:
			request.session['user'] = request.POST['username']
			return HttpResponseRedirect("/profile/")
		else:	
			return render(request, "home.html", {'error':'Either the username or the password is incorrect', 'form':LoginForm()})
			
		
def profile(request):
	global alert
	u = urlopen('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=21030&distance=100&API_KEY=40660235-9B2E-474F-B531-15EAB3B68EE0')
	j = load(u)
	d = {}
	for obj in j:
		 d[obj['ParameterName']] = obj['AQI']
	u = urlopen('http://agentk.pythonanywhere.com/weather')
	j = load(u)
	return render(request, "profile.html", {'user':request.session['user'], 'aqis':d, 'weather':j[j.keys()[-1]], 'pm':obj['AQI'], 'alert':alert})
	
	
def alert(request):
	global alert
	if request.POST['disease'] == 'lung cancer':
		if int(request.POST['aqi']) < 50:	
			alert = "It's not safe to step out"
		else:	
			alert = "It's safe to step out"	
	elif request.POST['disease'] == 'heart disease':
		if int(request.POST['aqi']) > 50 and int(request.POST['aqi']) < 100:	
			alert = "It's not safe to step out"
		else:	
			alert = "It's safe to step out"		
	elif request.POST['disease'] == 'asthma':
		if int(request.POST['aqi']) > 100:	
			alert = "It's not safe to step out"
		else:	
			alert = "It's safe to step out"
	return HttpResponseRedirect ("/profile/")
