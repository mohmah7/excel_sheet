from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Patient(models.Model):
    ptname = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.ptname
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient)
    diagnosis = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.diagnosis

class Hospital(models.Model):
    patient = models.ForeignKey(Patient)
    hospital_name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.hospital_name
