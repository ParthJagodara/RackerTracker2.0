from datetime import date, timedelta
from django.shortcuts import render_to_response
from django.http import *
from models import Racker, Workout
import json
from rackertracker.competitiondates import getRangeStart, getRangeEnd
from random import randint


def getPercentage():
    rackerlist = Racker.objects.all()
    total_workout = len(Workout.objects.all())
    print total_workout
    names = []
    counter = 0
    percentagelist = []
    start = getRangeStart()
    end = getRangeEnd()
    for racker in rackerlist:
        email = racker.email
        name = racker.name
        names.append(name)
        workouts = sumPersonalWorkouts(start,end,email)
        percentage = 100*float(workouts)/(float(total_workout))
        counter += percentage
        percentagelist.append(percentage)
        #temp = standing(email,workouts)
        #temp = standing(racker.email, sumPersonalWorkouts(start,end,racker.email)
       # cells.append(temp)
       # cells.append(temp)
    z = zip(percentagelist,names)
    sorted(z,reverse=True)
    return z 


def selectWinnerNow():
    start = getCurrentDates().start
    end = getCurrentDates().end
    workouts = Workout.objects.filter(date__gte = start, date__lte = end)
    print workouts
    print len(workouts)

    workout_count = Workout.objects.filter(id__gte=4).count()
    Winner_pick = Workout.objects.filter(id__gte=4).all()[randint(0, workout_count-1)]
    return Winner_pick.racker
    winner = Winner_pick.racker
    print winner.email

def getStanding():
    rackerlist = Racker.objects.all()
    names = []
    w = []
    start = getRangeStart()
    end = getRangeEnd()
    for racker in rackerlist:
        email = racker.email
        print email
        name = racker.name
        print name
        names.append(name)
        workouts = sumPersonalWorkouts(start,end,email)
        print workouts
        w.append(workouts)
        #temp = standing(email,workouts)
        #temp = standing(racker.email, sumPersonalWorkouts(start,end,racker.email)
       # cells.append(temp)
       # cells.append(temp)
    z = zip(w,names)
    sorted(z,reverse=True)
    return z 

def sumPersonalWorkouts(start,end,email):
    racker = Racker.objects.filter(email = email)
    workoutlist = Workout.objects.filter(date__gte = start, date__lte = end, racker= racker)
    return len(workoutlist)


#def GetWorkoutCells(workouts, start, end):
 #   r = Racker()
  #  cells = []
   # for w in workouts:
    #    if (w.racker.email != r.email):
     #       r = w.racker
      #      cell = WorkOutCell()
      #      cell__racker__(r)
      #      cell__num__(sumPersonalWorkouts(start, end, r))
      #      cells.append(cell)
    #return cells
