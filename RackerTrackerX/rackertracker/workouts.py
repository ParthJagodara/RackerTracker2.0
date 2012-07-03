from datetime import date, timedelta
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import *
from models import Racker, Workout
from rackertracker.racker import getRacker
from django.shortcuts import redirect
from django.db import IntegrityError

##
# Workouts Handler
def stats(request):
    response = HttpResponseNotAllowed(['GET', 'POST'])
    #racker = getRacker(email)
    
    #TODO: limit the date range
    standings = getStanding()

    max = 1
    for entry in standings:
        if entry[0] > max:
            max = entry[0]

    workouts=[]
    for entry in standings:
        count = entry[0]
        name = entry[1]
        scale = (100 * entry[0] / max)
        newEntry = {
            'name': name,
            'count': count,
            'scale': scale
            };
        workouts.append(newEntry)
    
    
    return render_to_response('workouts/stats.html', {'workouts': workouts, 'max': max}, context_instance=RequestContext(request))

def selectwinner(request):
    return render_to_response('workouts/selectwinner.html', context_instance=RequestContext(request))

def add(request):
    if request.method != 'POST':
        return "derp?"    
    email = request.POST['email']
    days = request.POST['days']
    racker1 = getRacker(email)
    for day in days:
        try:
            day = int(day)
            Workout.objects.create( date = date.today() - timedelta(days=day), racker = racker1)
        except IntegrityError:
            pass
    return redirect('/workouts')   

def rackerstats(request, email):
    return render_to_response('racker/stats.html', {'email': email}, context_instance=RequestContext(request))  

#
def getCurrentStanding():
    workouts = Workout.objects.all()
    
