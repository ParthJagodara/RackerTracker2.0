from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

rackerSelect = '([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})'
pastThreeDays = '(today|yesterday|two days ago)'
dateSelect = '([0-9]{2}-[0-9]{2}-[0-9]{4})'
racker = '(.+)'

urlpatterns = patterns('',
    url(r'^admin/[s|S]elect[w|W]inner', 'rackertracker.adminpages.selectwinner'),
    url(r'^admin/[q|Q]uery[r|R]acker', 'rackertracker.adminpages.queryRacker'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('rackertracker.views',
    #GET
    #(the hompage)
    url(r'^$', 'index'),
)

urlpatterns += patterns('rackertracker.ajax',
    url(r'^ajax/workouts/$', 'workouts'),
    url(r'^ajax/workouts/' + racker + '/' + dateSelect + '/' + dateSelect + '$', 'individual'),
)

urlpatterns += patterns('rackertracker.racker',
    #GET and POST
    #racker/create (post: name, email)
    #url(r'^racker/create$', 'create'),

    #GET and POST
    #racker/edit (post: name)
    url(r'^racker/' + rackerSelect + '/edit$', 'edit'),
    
    #POST
    #racker/{racker}/track/{days}
    url(r'^racker/' +  rackerSelect + '/track/' + pastThreeDays + '$', 'track'),

    #GET
    #racker/{racker}/stats
    #url(r'^racker/' +  rackerSelect + '/stats$', 'stats')
)


urlpatterns += patterns('rackertracker.workouts',

    #GET and POST
    #racker/edit (post: name)
    url(r'^workouts$', "stats"),
    #POST
    #selectwinner
    url(r'^workouts/add$', 'add'),

    #POST
    #selectwinner
    url(r'^workouts/' + rackerSelect + '$', 'rackerstats'),
)

#urlpatterns += patterns('rackertracker.workouts',
    #GET POST
    #workouts?start={date}&end={date}
#    url(r'^workouts$', 'workouts')
#)
