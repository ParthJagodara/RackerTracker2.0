from django.db import models

class Racker(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name + ', ' + self.email

    class Meta:
        unique_together = ('name', 'email')
    
class Workout(models.Model):
    racker = models.ForeignKey(Racker)
    date = models.DateField()
    
    def __unicode__(self):
        return str(self.racker) + ', ' + unicode(self.date)

    class Meta:
        unique_together = ('racker', 'date')

class CompanyLunch(models.Model):
    date = models.DateField()

    def __unicode__(self):
        return 'Company Lunch ' + unicode(self.date)

class Winner(models.Model):
    racker = models.ForeignKey(Racker)
    date = models.ForeignKey(CompanyLunch)

    def __unicode__(self):
        return self.racker.name + ' won ' + unicode(self.date)

class Badge(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField('Description')
    rackers = models.ManyToManyField(Racker, blank=True)

    def __unicode__(self):
        return self.title
