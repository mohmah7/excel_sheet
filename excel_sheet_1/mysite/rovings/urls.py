from django.conf.urls import patterns, url

from rovings import views

"""urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)"""

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.get_name, name='index'),
    #url(r'^search_form/$', views.search_form, name ='search_form'),
    url(r'^add_pt/$', views.add_pt),
    url(r'^manage_patients/$',views.manage_patients),
    url(r'^hello/$', views.hello, name='hello'),
    # ex: /polls/5/
    url(r'^(?P<patient_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<patient_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<patient_id>\d+)/vote/$', views.vote, name='vote'),
)