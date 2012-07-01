from django.http import *
from django.utils import simplejson
from rackertracker.models import Racker, Workout, CompanyLunch
from rackertracker.competitiondates import getRangeEnd
from operator import itemgetter
from datetime import datetime
from django.db import IntegrityError

def workouts(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)
        try:
            r = Racker.objects.get(email = email)
        except DoesNotExist:
            r = Racker.objects.create(name = email, email = email)
        exlist = range(3)
        for num in exlist:
            exercise = request.POST.get('exercise[' + unicode(num) + ']', False)
            if exercise != False:
                try:
                    d = datetime.fromtimestamp(int(exercise)/1000)
                    print(d)
                except ValueError:
                    print('error')
                print(r)
                try:
                    w = Workout.objects.create(racker = r, date = d)
                    print(w)
                except IntegrityError:
                    print('integrity error caught, workout exists')
    if request.method == 'POST' or request.method == 'GET':
        return HttpResponse(simplejson.dumps(standing()), mimetype="application/json")

def standing():
    response_data = {}
    response_data['month'] = getRangeEnd().strftime('%B')
    response_data['year'] = getRangeEnd().year
    print(response_data)
    orderedLunches = CompanyLunch.objects.order_by('date')
    startDate = orderedLunches[0].date
    endDate = orderedLunches[1].date
    workoutsInRange = Workout.objects.filter(date__gte = startDate, date__lte = endDate)
    rackers = Workout.objects.values_list('racker', flat=True).distinct()
    users = list()
    for rackerID in rackers:
        user = {}
        tempRacker = Racker.objects.get(pk=rackerID)
        user['email'] = tempRacker.email
        user['score'] = workoutsInRange.filter(racker=tempRacker).count()
        users.append(user)
    response_data['users'] = sorted(users, key=itemgetter('score'), reverse=True)
    return response_data
