from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms.models import modelform_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from rovings.models import Patient , Diagnosis, Hospital

def index(request):
    latest_poll_list = Patient.objects.all().order_by('-admission_date')
    #p= Patient(ptname ="mefnamicacid",pub_date=timezone.now())
    #p.save()
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'rovings/index.html', context)


def detail(request, patient_id):
    return HttpResponse("You're looking at poll %s." % patient_id)

def detail(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise Http404
    return render(request, 'rovings/detail.html', {'patient': patient})

def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'rovings/detail.html', {'patient': patient})

def results(request, patient_id):
    return HttpResponse("You're looking at the results of poll %s." % patient_id)

def vote(request, patient_id):
    return HttpResponse("You're voting on poll %s." % patient_id)

def hello(request):
    return HttpResponse("Hello world")

def search_form(request):
    return render(request, 'rovings/add_pt.html')

def add_pt(request):

    msg_diagnosis=''
    msg_hospital =''
    #if 'q' in request.GET:

    if 'q' in request.GET:
        #message = 'You searched for: %r' % request.POST['q']
        message = request.GET['q']
        msg_diagnosis = request.GET['p']
        msg_hospital=request.GET['h']
        p = Patient(ptname = message,pub_date=timezone.now())
        p.save()
        p.diagnosis_set.create(diagnosis=msg_diagnosis)
        p.hospital_set.create(hospital_name=msg_hospital)
        return HttpResponseRedirect(reverse('rovings:index'))

    else:
        message = 'You submitted an empty form.'
        return render(request, "rovings/add_pt.html",{'message':message})

    #if 'p' in request.POST:
        #msg_diagnosis = request.POST['p']
    #msg_hospital = request.POST['h']


    #return HttpResponse(message)
    #return render(request, "rovings/add_pt.html",{'message':message,'msg_diagnosis':msg_diagnosis})

def manage_patients(request, patient_id=None):
    patient = None
    diagnosis = None
    hospital = None
    message = "Saving new patient"
    if patient_id:
        patient = get_object_or_404(Patient, pk=patient_id)
        diagnosis = get_object_or_404(Diagnosis , pk=patient_id)
        hospital = get_object_or_404(Hospital)

    PatientForm = modelform_factory(Patient)
    DiagnosisForm = modelform_factory(Diagnosis, fields =('diagnosis',))
    HospitalForm = modelform_factory(Hospital, fields = ('hospital_name',))
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        form_diagnosis = DiagnosisForm(request.POST, instance = diagnosis)
        form_hospital = HospitalForm(request.POST, instance = hospital)
        if form.is_valid() & form_diagnosis.is_valid() & form_hospital.is_valid():
            patient = form.save()
            patient_diagnosis = form_diagnosis.save(commit = False)
            patient_hospital = form_hospital.save(commit = False)
            patient_diagnosis.patient=patient
            patient_hospital.patient = patient
            patient_diagnosis.save()
            patient_hospital.save()
            message = "Successfuly saved patient"
            return HttpResponseRedirect(reverse('rovings:patient_edit', kwargs={'patient_id':str(patient.pk)}))   
    else:
        form = PatientForm(instance=patient)
        form_diagnosis = DiagnosisForm(instance=diagnosis)
        form_hospital = HospitalForm(instance = hospital)

    if patient:
        message = "Editing patient"

    return render(request, "rovings/add_pt.html", {"form": form, 'message':message, 'form_diagnosis':form_diagnosis, 'form_hospital':form_hospital,})

"""class MyFormView(View):
    form_class = Patient
    initial = {'key': 'value'}
    template_name = 'rovings/add_pt.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def manage_patients(request, patient_id=None):
        patient = None
        diagnosis = None
        message = "Saving new patient"
        if patient_id:
            patient = get_object_or_404(Patient, pk=patient_id)
            diagnosis = get_object_or_404(Diagnosis , pk=patient_id)

        PatientForm = modelform_factory(Patient)
        DiagnosisForm = modelform_factory(Diagnosis, fields =('diagnosis','votes',))
        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)
            form_diagnosis = DiagnosisForm(request.POST, instance = diagnosis)
            if form.is_valid() & form_diagnosis.is_valid():
                patient = form.save()
                patient_diagnosis = form_diagnosis.save(commit = False)
                patient_diagnosis.patient=patient
                patient_diagnosis.save()
                message = "Successfuly saved patient"
                return HttpResponseRedirect(reverse('rovings:patient_edit', kwargs={'patient_id':str(patient.pk)}))
        else:
            form = PatientForm(instance=patient)
            form_diagnosis = DiagnosisForm(instance=diagnosis)

        if patient:
            message = "Editing patient"

        return render(request, "rovings/add_pt.html", {"form": form, 'message':message, 'form_diagnosis':form_diagnosis})"""