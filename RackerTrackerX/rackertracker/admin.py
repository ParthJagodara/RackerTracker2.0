from rackertracker.models import Racker, Workout, Winner, CompetitionDates
from django.contrib import admin

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('racker', 'date')
    list_filter = ('date',)

class RackerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')

class WinnerAdmin(admin.ModelAdmin):
    list_display = ('racker', 'date')

class CompetitionDatesAdmin(admin.ModelAdmin):
    list_display = ('start', 'end')

admin.site.register(Racker, RackerAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Winner, WinnerAdmin)
admin.site.register(CompetitionDates, CompetitionDatesAdmin)
