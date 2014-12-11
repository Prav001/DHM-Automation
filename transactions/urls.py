from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views import generic
from django.conf.urls.static import static
from filters import views
from transactions.views import get_details,tranresults


urlpatterns = patterns('',
    url(r'^/$',get_details),
    url(r'^/results/$',tranresults),                   
                       )



