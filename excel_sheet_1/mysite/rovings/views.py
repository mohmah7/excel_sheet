from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from rovings.models import Patient , Diagnosis, Hospital
from django.shortcuts import render
from django.http import Http404

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def index(request):
    latest_poll_list = Patient.objects.order_by('-pub_date')[:5]
    #p= Patient(ptname ="mefnamicacid",pub_date=timezone.now())
    #p.save()
    template = loader.get_template('rovings/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def index(request):
    latest_poll_list = Patient.objects.all().order_by('-pub_date')[:5]
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


from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.utils import timezone

def hello(request):
    return HttpResponse("Hello world")

"""def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Patient(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            content = form.cleaned_data['ptname']
            post = m.Post.objects.create(ptname=ptname)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Patient()

    return render(request, 'rovings/index.html', {'form': form})"""

def search_form(request):
    return render(request, 'rovings/search_form.html')

from django.views import generic

def search(request):
    msg_diagnosis=''
    msg_hospital =''
    if 'q' in request.GET:
        #message = 'You searched for: %r' % request.POST['q']
        message = request.GET['q']
        msg_diagnosis = request.GET['p']
        msg_hospital=request.GET['h']
        p = Patient(ptname = message,pub_date=timezone.now())
        p.save()
        p.diagnosis_set.create(diagnosis=msg_diagnosis)
        p.hospital_set.create(hospital_name=msg_hospital)

    else:
        message = 'You submitted an empty form.'

    #if 'p' in request.POST:
        #msg_diagnosis = request.POST['p']
    #msg_hospital = request.POST['h']


    #return HttpResponse(message)
    return render(request, "rovings/search_form.html",{'message':message,'msg_diagnosis':msg_diagnosis})
