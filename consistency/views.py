from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
from consistency.models import DHM_Consis_Repository,DHM_Consis_Report
from django_tables2 import RequestConfig
from consistency.tables import ConsisTable,ConsisReport
from consistency.forms import ConsistencyForm
from consistency.models import DHM_Consis_Repository ,DHM_Consis_Report
from masters.models import Customer
import mimetypes
import os
import glob
from django.core.servers.basehttp import FileWrapper
import xlwt
from datetime import date
import pandas as ps
from django_pandas.io import read_frame
from django.db.models import Q
import pyodbc


stat1=("exec consis_report_population ?,?,?,?,?,?")
global customername

@login_required            
def consisreportgen(request):
    if request.method == 'POST':
        form = ConsistencyForm(request.POST or None)
        if form.is_valid():
            customername=request.POST.get('Customer','')
            modules_choosen=request.POST.getlist('Modules','')
            bpc_choosen=request.POST.getlist('Components','')
            severity=request.POST.get('Severity_level','')
            run_date=request.POST.get('run_date','')
            min_count=request.POST.get('min_count','')
            Customer=form.cleaned_data.get('Customer')
            Components=form.cleaned_data.get('Components')
            Modules=form.cleaned_data.get('Modules')
            run_date=form.cleaned_data.get('run_date')
            min_count=form.cleaned_data.get('min_count')
            print(modules_choosen)
            print(customername)
            print(severity)
            print(run_date)
            print(min_count)
            for x in range(len(bpc_choosen)):
                print(bpc_choosen[x])
            for y in range(len(modules_choosen)):
                print(modules_choosen[y])
            cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=RAMCOBL267;DATABASE=testing;UID=sa;PWD=development12$')
            cursor = cnxn.cursor()
            cursor.execute("DELETE FROM dhm_consis_report_tbl")
            for x in range(len(bpc_choosen)):
                for y in range(len(modules_choosen)):
                    cursor.execute(stat1,customername,bpc_choosen[x],modules_choosen[y],severity,run_date,min_count)
            cursor.commit()       
            
            
            return HttpResponseRedirect('/consistency/results/')
        
    else:
        form = ConsistencyForm
        
    return render(request,'consistency/consistency.html', {'form': form})
        

@login_required
def consisreports(request):
    cust= customername
    username=None
    if request.user.is_authenticated():
        username=request.user.username
    print(username)    
    table=ConsisReport(DHM_Consis_Report.objects.all())
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    todays=date.today()
    todays=todays.strftime("%d-%m-%y")
    filename="Consistency Report %s as on %s %s.xls"%(cust,str(todays),username)   
    colname=['Customer','Query ','Count','Desc','Criticality','Status','Rundate','Instance ID']
    try:
        df = ps.DataFrame.from_records(DHM_Consis_Report.objects.values('conquery_source','conquery_name','conquery_count','conquery_desc','criticality','sp_status','con_rundate','instance_id'))
        df=df[['conquery_source','conquery_name','conquery_count','conquery_desc','criticality','sp_status','con_rundate','instance_id']]
        print(df)
        writer = ps.ExcelWriter('C:/Python34/Scripts/automation/files/%s'%filename)
        df.to_excel(writer,sheet_name='Report',index=False,engine='xlsxwriter',header=colname)
        writer.save()
    except KeyError:
        print("Key Error Occured")
        
    return render(request, 'consistency/consresult.html', {'table': table,'customername':cust})
             
          
@login_required       
def  export_excel(request):
    custname=customername
    username=None
    if request.user.is_authenticated():
        username=request.user.username
    todays=date.today()
    todays=todays.strftime("%d-%m-%y")
    filename="Consistency Report %s as on %s %s.xls"%(custname,str(todays),username)
    wrapper=open('C:/Python34/Scripts/automation/files/%s'%filename,"rb")
    cont=wrapper.read()
    response = HttpResponse(cont,content_type="application/vnd.ms-excel;charset=utf-8")
    response['Content-Length']=os.path.getsize('C:/Python34/Scripts/automation/files/%s'%filename)
    size=os.path.getsize('C:/Python34/Scripts/automation/files/%s'%filename)
    print(size)
    wrapper.close()
    response['Content-Disposition'] = 'attachment; filename= %s'%filename
    return response

    
    

    

    
    
    
    
    
   
        
           
            
            
            
    

    
  
        
