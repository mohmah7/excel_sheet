from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.forms.models import modelform_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.core.urlresolvers import reverse

from rovings.models import Patient , Diagnosis, Hospital

def index(request):
    latest_poll_list = Patient.objects.all().order_by('-pub_date')
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
    message = "Saving new patient"
    if patient_id:
        patient = get_object_or_404(Patient, pk=patient_id)

    PatientForm = modelform_factory(Patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save()
            message = "Successfuly saved patient"
            return HttpResponseRedirect(reverse('rovings:patient_edit', kwargs={'patient_id':str(patient.pk)}))   
    else:
        form = PatientForm(instance=patient)

    if patient:
        message = "Editing patient"

    return render(request, "rovings/add_pt.html", {"form": form, 'message':message})
