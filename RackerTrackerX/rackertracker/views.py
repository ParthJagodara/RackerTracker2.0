from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from rackertracker.racker import getRacker
from rackertracker.models import Workout, Racker
from datetime import date, timedelta

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))         

def bootstrapIndex(request):
    return render_to_response('indexc.html', context_instance=RequestContext(request)) 
