from rackertracker.models import CompanyLunch

def getRangeStart():
    start = CompanyLunch.objects.order_by('date')
    return start[0].date

def getRangeEnd():
    end = CompanyLunch.objects.order_by('date')
    return end[1].date

def getAllDatesInOrder():
    dates = CompetitionDates.objects.sort_by('-end')
    return dates

def getLastNumberOfDates(numDates):
    dates = getAllDatesInOrder()
    return dates[:numDates]
