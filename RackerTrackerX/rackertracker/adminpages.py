from django.template import RequestContext
from django.shortcuts import render_to_response
from rackertracker.ajax import standing, month_total

def selectwinner(request):
    data = standing()
    for user in data['users']:
        user['percent'] = str(float(user['score'])/float(month_total()) * 100) + '%'
    return render_to_response("adminselectwinner.html", RequestContext(request, data))

def queryRacker(request):
    return render_to_response("adminqueryracker.html")
