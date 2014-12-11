from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from ajax_select import urls as ajax_select_urls
from home.views import HomePageView #,home_page


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view()),                   
    url(r'^home', include('home.urls')),
    url(r'^filters', include('filters.urls')),
    url(r'^consistency', include('consistency.urls')),
    url(r'^transactions', include('transactions.urls')),                   
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/lookups/', include(ajax_select_urls)),                   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),                                    
    url(r'^grappelli/', include('grappelli.urls')),
    ) 
