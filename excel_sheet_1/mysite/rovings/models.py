from django.db import models
from django.utils import timezone
import datetime

# Create your models here.



class Patient(models.Model):
    JUSTIFICATION = (
        ('JS', 'Justified'),
        ('UNJ', 'UnJusitfied'),
    )
    ptname = models.CharField(max_length=100)
    visit_date = models.DateField('date visited')
    admission_date = models.DateField('Admission Date')
    discharge_date = models.DateField('Discharge Date')
    app_number = models.CharField(max_length =20, default = None)
    age = models.PositiveIntegerField(default =0)
    days_requested = models.PositiveIntegerField(default = 0)
    days_approved = models.PositiveIntegerField(default =0)
    policy_number = models.PositiveIntegerField(default =0)
    notes = models.TextField(max_length=2000, blank = True)
    justified = models.CharField(max_length =15, choices = JUSTIFICATION)
    benefit_lower_limit = models.CharField(max_length = 15, default ='Nil')
    benefit_upper_limit = models.CharField(max_length = 15, default = 'Nil')
    benifit = models.CharField(max_length = 15, default = 'Nil')
    app_doctor = models.CharField(max_length = 20, default = 'Dr. Mohamed Mahmoud')
    initiator = models.CharField(max_length = 20, default = 'RC UP')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.ptname
    """def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'"""

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient)
    diagnosis = models.CharField(max_length=100)
    def __unicode__(self):
        return self.diagnosis

class Hospital(models.Model):
    HOSPITAL_CHOICES = (
    ('ASTOON','Astoon'),
    ('AL DOSSARY','AlDossary'),
    ('FAKHRY','Fakhry'),
    ('AL MANA','Al Mana'),
    ('AL YOUSEF','Al Yousef'),
    ('AL SALAMA','Al Salama'),
    )
    patient = models.ForeignKey(Patient)
    hospital_name = models.CharField(max_length = 100, choices=HOSPITAL_CHOICES)
    def __unicode__(self):
        return self.hospital_name
