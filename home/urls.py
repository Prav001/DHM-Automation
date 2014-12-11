from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from home.views import about_view,faq_view

from home.views import HomePageView
#from home.views.HomePageView import home

from ajax_select import urls as ajax_select_urls


urlpatterns = patterns('',
   # url(r'^/$',home_page),
    url(r'^/$',HomePageView.as_view()),                   
    url(r'^/about/$',about_view),
    url(r'^/faq/$',faq_view)
                       )
                       
                       
                       
