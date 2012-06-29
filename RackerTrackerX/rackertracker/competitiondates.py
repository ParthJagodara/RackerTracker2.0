from rackertracker.models import CompetitionDates

def getCurrentDates():
    date = CompetitionDates.objects.latest('end')
    return date

def getAllDatesInOrder():
    dates = CompetitionDates.objects.sort_by('-end')
    return dates

def getLastNumberOfDates(numDates):
    dates = getAllDatesInOrder()
    return dates[:numDates]
