from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views import generic
from django.conf.urls.static import static
from filters import views
from consistency.views import consisreportgen,consisreports,export_excel

urlpatterns = patterns('',
    url(r'^/$',consisreportgen,name='Consistency'),
    url(r'^/results/$',consisreports,name='Consistency result'),
    url(r'^/generate/$',export_excel,name='Generate Excel'),                   
                      
                       
                       )

