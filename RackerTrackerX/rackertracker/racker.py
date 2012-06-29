from datetime import date, timedelta
from django.shortcuts import render_to_response
from django.http import *
from models import Racker, Workout

def index(request):
    return HttpResponse('do want to be able to call rackers?')
##
# Racker Create Handler
def create(request):
    if request.method == 'GET':
        return HttpResponse("write this form. lol")
    elif request.method == 'POST':
        return HttpResponse("I don't know how to save that data yet.")
    else:
        return HttpResponse("lolwut?")

##
# Racker Edit Handler
def edit(request, email):
    response = HttpResponseNotAllowed(['GET', 'POST'])

    # fetch racker
    racker = getRacker(email)
    if request.method == 'GET':
        response = render_to_response('racker/edit.html', {'racker': racker})
    elif request.method == 'POST':
        # FIXME: create post response
        racker.name = request.POST.get('name')
    return response

##
# Racker Track Handler
def track(request, email):
    response = HttpResponseNotAllowed(['GET', 'POST'])
   
    #fetch racker
    racker = getRacker(email)
    if request.method == 'GET':
        response = render_to_response('racker/track.html', {'racker': racker})
    #elif request.method == 'POST':
       # days = request.POST.get['days']
       # for day in days

    else:
        return HttpResponse("lolwut?")

##
# Racker Stats Handler
def index(request, email):
    response = HttpResponseNotAllowed(['GET', 'POST'])

    # fetch racker
    racker = getRacker(email)
    if request.method == 'GET':
        response = render_to_response('racker/track.html', {'racker': racker1})
    else:
        return HttpResponse("lolwut?")

##
# Get Racker Utility Method
def getRacker(racker_email):
    racker_email = racker_email.lower()
    racker_email = racker_email.replace("mailtrust.com", "rackspace.com")

    defaultName = racker_email[:racker_email.find("@")]
    # try to fetch Racker, if Racker does not exist create one using the email
    try:
        racker = Racker.objects.get(email = racker_email)
    except Racker.DoesNotExist:
        racker = Racker.objects.create(name = defaultName, email = racker_email)
    
    return racker

##
# Utility method for parsing date string
# FIXME: move to a utility class
def parseDate(date):
    if date == "today":
        return date.today()
    if date == "yesterday":
        return date.today() - timedelta(days=1)
    if date == "two days ago":
        return date.today() - timedelta(days=2)
    return "invalid date"

