from __future__ import unicode_literals
from __future__ import print_function, division, absolute_import, unicode_literals
from django.shortcuts import render, redirect, get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.models import Graphs
from home.charts import chartdata
from masters.models import Customer
from django.db.models import Count
from django.db.models import Max




class HomePageView(TemplateView):
    template_name = 'home/homepage.html'
    
    @method_decorator(login_required)

    def dispatch(self, *args,**kwargs):
        return super(HomePageView, self).dispatch(*args,**kwargs)





    def get_context_data(self, **kwargs):
    		# return HttpResponse ('home')
        # lu = { 'categories' : [ 'Jan 2014', 'Mar 2014','Jun 2014', 'Aug 2014', 'Oct 2014', 'Dec 2014'],\
        #      'undergrad' : [18, 22, 30, 34, 40, 47],\
        #      'grad' : [1, 2, 4, 4, 5, 7],\
        #      'employee' : [2, 3, 0, 1, 1, 2] }
        # lu['total_enrolled'] = [sum(a) for a in zip(lu['undergrad'], lu['grad'],lu['employee'])]
        #lu['total_count']=Graphs.objects.all().count()
        
        lu = {}
        q=Customer.objects.values('cust_name')
        custno=len(q)
        cts = Graphs.objects.all().aggregate(Max('total_count'))
        maxno = Graphs.objects.latest('total_count')
       
        print(maxno)
        


       
        amt=0
        for i in Graphs.objects.all():
            amt+=i.total_count
        lu['total_count'] = amt

       
        lu['date'] = chartdata.get_date_wise()
        lu['ct'] = chartdata.get_count_wise()
        lu['cust'] =  chartdata.get_cust_wise()

        lu['air'] = chartdata.get_air_wise()
        lu['aero'] = chartdata.get_aero_wise()
        lu['total_cust']=custno
        lu['max_count'] = maxno


        print (lu)

        #return render_to_response('mypolls/polls_chart.html', lu )
        #polls_chart.allow_tags = True
        context=lu

        return context        
        
     
        

##def home_page(request):
##    
##    template = 'home/homepage.html',
##    return render(request,template)
    
@login_required
def about_view(request):
    template='home/about.html',
    return render(request,template)

@login_required
def faq_view(request):
    template='home/faq.html',
    return render(request,template)
