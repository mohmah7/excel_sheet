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
    extra = 2



class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ptname']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [DiagnosisInline, HospitalInline]
    list_display = ('ptname', 'pub_date')
    list_filter = ['ptname']
    search_fields = ['ptname']

"""class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ptname']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]"""

admin.site.register(Patient,PollAdmin)

#admin.site.register(Diagnosis)

#admin.site.register(Hospital)