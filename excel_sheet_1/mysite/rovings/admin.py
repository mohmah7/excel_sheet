from django.contrib import admin
from rovings.models import  Patient, Diagnosis, Hospital

# Register your models here.

"""class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'ptname']"""


"""class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ptname']}),
        ('Date information', {'fields': ['pub_date']}),
    ]"""

class DiagnosisInline(admin.TabularInline):
    model = Diagnosis
    extra = 3

class HospitalInline(admin.TabularInline):
    model = Hospital
    extra = 0



class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ptname']}),
        ('Visit Date', {'fields': ['visit_date'], 'classes': ['collapse']}),
        ('Approval Number',{'fields':['app_number']}),
        ('Admission Date', {'fields': ['admission_date']}),
        ('Discharge Date', {'fields':['discharge_date']}),
        ('Age', {'fields': ['age']}),
        ('Days Requested', {'fields':['days_requested']}),
        ('Days Approved', {'fields':['days_approved']}),
        ('GRH',{'fields':['policy_number']}),
        ('Notes',{'fields':['notes']}),
        ('Justified',{'fields':['justified']}),
        ('Benifit Lower Limit',{'fields':['benefit_lower_limit']}),
        ('Benefit Upper Limit',{'fields':['benefit_upper_limit']}),
        ('Benefit',{'fields':['benifit']}),
        ('Approval Doctor',{'fields':['app_doctor']}),
        ('Initiator',{'fields':['initiator']}),

    ]
    inlines = [DiagnosisInline, HospitalInline]
    list_display = ('ptname', 'visit_date','app_number')
    list_filter = ['ptname']
    search_fields = ['ptname']

"""class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ptname']}),
        ('Date information', {'fields': ['visit_date'], 'classes': ['collapse']}),
    ]"""

admin.site.register(Patient,PollAdmin)

#admin.site.register(Diagnosis)

#admin.site.register(Hospital)