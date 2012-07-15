from rackertracker.models import Racker, Workout, Winner, CompanyLunch
from django.contrib import admin
from django import forms

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('racker', 'date')
    list_filter = ('date',)

class RackerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')

class WinnerAdmin(admin.ModelAdmin):
    list_display = ('racker', 'date')

class CompanyLunchAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(Racker, RackerAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Winner, WinnerAdmin)
admin.site.register(CompanyLunch, CompanyLunchAdmin)

class QueryRackerForm(forms.Form):
    emails = list()
    for racker in Racker.objects.all():
        emails.append(racker.email)
    print(emails)
    racker = forms.ChoiceField(choices=(emails))
    startDate = forms.DateField()
    endDate = forms.DateField()
