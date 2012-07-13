from django.template import RequestContext
from django.shortcuts import render_to_response
from rackertracker.workouthelper import getPercentage

def selectwinner(request):
    return render_to_response("adminselectwinner.html", RequestContext(request, {'list': getPercentage()}))

def queryRacker(request):
    return render_to_response("adminqueryracker.html")
