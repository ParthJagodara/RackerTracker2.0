from django.http import *
from django.utils import simplejson
from rackertracker.models import Racker, Workout, CompanyLunch
from rackertracker.competitiondates import getRangeEnd
from operator import itemgetter
from datetime import datetime

def workouts(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)
        try:
            r = Racker.objects.get(email = email)
        except DoesNotExist:
            createRacker = []
        exlist = [ 0, 1, 2 ]
        for num in exlist:
            exercise = request.POST.get('exercise[' + unicode(num) + ']', False)
            if exercise:
                d = datetime.fromtimestamp(exercise)
                w = Workout.objects.create(racker = r, date = d)
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
