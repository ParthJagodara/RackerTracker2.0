from django.template import RequestContext
from django.shortcuts import render_to_response
from rackertracker.workouthelper import getPercentage
from rackertracker.admin import QueryRackerForm

def selectwinner(request):
    return render_to_response("adminselectwinner.html", RequestContext(request, {'list': getPercentage()}))

def queryRacker(request):
    form = QueryRackerForm()
    return render_to_response("adminqueryracker.html", {'form': form})
