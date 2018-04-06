import datetime
from django.db import models
from django.utils import timezone

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name +' '+ self.last_name
    def __unicode__(self):
        return '%d: %s' % (self.first_name, self.last_name)

class Album(models.Model):
    artist = models.ForeignKey(Musician, related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    def __str__(self):
        return self.name
    def __unicode__(self):
        return '%d' % (self.name)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)

    def __str__(self):
        return self.title