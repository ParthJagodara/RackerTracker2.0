from rackertracker.models import Racker, Workout, Winner, CompanyLunch, Badge
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

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('title','desc')
    filter_horizontal = ('rackers',)


admin.site.register(Racker, RackerAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Winner, WinnerAdmin)
admin.site.register(CompanyLunch, CompanyLunchAdmin)
admin.site.register(Badge, BadgeAdmin)
