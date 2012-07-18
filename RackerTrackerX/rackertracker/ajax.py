from django.http import *
from django.utils import simplejson
from rackertracker.models import Racker, Workout, CompanyLunch, Winner
from rackertracker.competitiondates import getRangeEnd
from operator import itemgetter
from datetime import datetime
from django.db import IntegrityError

def workouts(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)
        try:
            r = Racker.objects.get(email = email)
        except Racker.DoesNotExist:
            name = email.split('@')[0]
            r = Racker.objects.create(name = name, email = email)
        exlist = range(3)
        for num in exlist:
            exercise = request.POST.get('exercise[' + unicode(num) + ']', False)
            if exercise != False:
                try:
                    d = datetime.fromtimestamp(int(exercise)/1000)
                except ValueError:
                    print('error')
                try:
                    w = Workout.objects.create(racker = r, date = d)
                except IntegrityError:
                    print('integrity error caught, workout exists')
    if request.method == 'POST' or request.method == 'GET':
        return HttpResponse(simplejson.dumps(standing()), mimetype="application/json")

def standing():
    response_data = {}
    response_data['month'] = getRangeEnd().strftime('%B')
    response_data['year'] = getRangeEnd().year
    orderedLunches = CompanyLunch.objects.order_by('date')
    startDate = orderedLunches[0].date
    endDate = orderedLunches[1].date
    workoutsInRange = Workout.objects.filter(date__gte = startDate, date__lte = endDate)
    rackers = Workout.objects.values_list('racker', flat=True).distinct()
    users = list()
    for rackerID in rackers:
        user = {}
        tempRacker = Racker.objects.get(pk=rackerID)
        user['email'] = tempRacker.name
        user['score'] = workoutsInRange.filter(racker=tempRacker).count()
        users.append(user)
    response_data['users'] = sorted(users, key=itemgetter('score'), reverse=True)
    return response_data

def users(response):
    orderedLunches = CompanyLunch.objects.order_by('date')
    startDate = orderedLunches[0].date
    endDate = orderedLunches[1].date
    workoutsInRange = Workout.objects.filter(date__gte = startDate, date__lte = endDate)
    rackers = Workout.objects.values_list('racker', flat=True).distinct()
    rack = list()
    for racker in rackers:
        user = {}
        user['name'] = Racker.objects.get(pk=racker).name
        rack.append(user)
    data = {}
    data['users'] = rack
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def month_total():
    orderedLunches = CompanyLunch.objects.order_by('date')
    startDate = orderedLunches[0].date
    endDate = orderedLunches[1].date
    return Workout.objects.filter(date__gte = startDate, date__lte = endDate).count()

def individual(request, user, start, end):
    dateFormat = '%m-%d-%Y'
    if request.method == 'GET':
        #need to define start and end
        email = user.strip() + '@mailtrust.com'
        orderedLunches = CompanyLunch.objects.order_by('date')
        startDate = datetime.strptime(start, dateFormat)
        endDate = datetime.strptime(end, dateFormat)
        workoutsInRange = Workout.objects.filter(date__gte = startDate, date__lte = endDate)
        try:
            r = Racker.objects.get(email = email)
            rackerWorkouts = workoutsInRange.filter(racker = r).count()
        except Racker.DoesNotExist:
            rackerWorkouts = 0
        data = {}
        data['workouts'] = rackerWorkouts
        return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def wins(request, user):
    if request.method == 'GET':
        email = user.strip() + '@mailtrust.com'
        wins = {}
        data = list()
        try:
            racker = Racker.objects.get(email = email)
            winnings = Winner.objects.filter(racker = Racker.objects.get(email=email))
            for win in winnings:
                item = {}
                item['won'] = datetime.strftime(win.date.date, '%m-%d-%Y')
                data.append(item)
            wins['wins'] = data
        except Racker.DoesNotExist:
            wins['wins'] = data
        return HttpResponse(simplejson.dumps(wins), mimetype="application/json")
