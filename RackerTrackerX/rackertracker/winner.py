from datetime import date, timedelta
from django.shortcuts import render_to_response
from django.http import *
from models import Winner

def results(request):
    if request.method == 'GET':
        return render_to_response("winners.html", {'winners' : Winner.objects.all()})

