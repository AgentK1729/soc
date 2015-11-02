from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from forms import *
from django.contrib.auth.models import User

def home(request):
	if request.method == 'GET':
		return render(request, "home.html", {'static':settings.STATIC_URL, 'form':LoginForm()})
	elif request.method == 'POST':
		u = User.objects.get(username=request.POST['username'])
		if u.password == request.POST['password']:
			return HttpResponse("Done")
		else:	
			return HttpResponse("Not done")
