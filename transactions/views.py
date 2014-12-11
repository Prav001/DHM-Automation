from django.shortcuts import render, redirect, get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from transactions.forms import TranForm
from transactions.models import TranStats
from transactions.tables import Trantable
from django_tables2 import RequestConfig
from masters.models import Customer
from django.db.models import Q
import pyodbc

@login_required
def tranresults(request):
    table=Trantable(TranStats.objects.all())
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    return render(request, 'transactions/tranresult.html',{'table': table})

@login_required
def get_details(request):
    
    if request.method == 'POST':
        form=TranForm(request.POST)
        if form.is_valid():
            client=Customer.objects.all()
            customer=request.POST.get("customer_name","")
            fromdate=request.POST.get("from_date","")
            todate=request.POST.get("to_date","")
            customer=form.cleaned_data.get('customer')
            fromdate=form.cleaned_data.get('fromdate')
            todate=form.cleaned_data.get('todate')
            conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=RAMCOBL267;DATABASE=AVNAPPDB;UID=sa;PWD=development12$')
            cursor = conn.cursor()
            cursor.execute("insert into myttable values(6,48)")
            cursor.execute("exec avnappdb.dbo.cmn_transaction_stats_sp ?,?",fromdate,todate)
            cursor.execute("select * from cust_tran_stats")
            cursor.commit()
            print(customer)
            print(fromdate)
            print(todate)
            return HttpResponseRedirect('/transactions/results')
    else:
        form=TranForm()
        errors=form.errors or None

    return render(request,'transactions/trans.html',{
        'form':form,
        'errors':errors,
    })
        

        
    
    
        
    
          

   

            
              
                
               

    
        
            
        



    
    
    
        
    
        
                  
                
                   
                
        
        
    
    
