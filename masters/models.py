from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.



class Customer(models.Model):

    INDIA='India'
    ASIAPAC='Asia Pacific'
    MIDDLEEAST='Middle East'
    AMERICA='USA'
    EUROPE='Europe'
    CANADA='Canada'
    REGION_ALL=((INDIA,'India'),
                (ASIAPAC,'Asia Pacific'),
                (AMERICA,'USA'),
                (EUROPE,'Europe'),
                (CANADA,'Canada'),
                (MIDDLEEAST,'Middle East'))
                
    
    cust_geo=models.CharField("Geography",max_length=40,choices=REGION_ALL)
    cust_name=models.CharField("Customer Name",primary_key=True,max_length=40)
    
    cust_code=models.CharField("Customer Code",max_length=40)
    cust_supp_coordi=models.CharField("Support Corrdinator",max_length=40)
    cust_part_id = models.CharField("Partner ID",max_length=40,blank=True)
##    custmodule = models.ForeignKey(Modules)
    is_active  = models.BooleanField("Customer Status",help_text='Customer is in active state or not',default=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField("Updated by",max_length=100)
    added_by = models.CharField("Added by",max_length=100)
    
    class Meta:
        verbose_name_plural = 'Customer Registration'
        db_table='dhm_cust_dtl'
    

    def __str__(self):
        return u'{0}'.format(self.cust_name)
    
   
        

class  Criticality(models.Model):
    NONCRITICAL ='Noncritical'
    CRITICAL = 'Critical'
    ALL= 'All'
    CRITIC_ALL =((NONCRITICAL, 'Noncritical'),
          (CRITICAL,'Critical'),
           (ALL,'All'))
           
    severity=models.CharField(primary_key=True,max_length=80,choices=CRITIC_ALL)

    class Meta:
       verbose_name_plural = 'Severity'
       db_table='dhm_sev'
    

    def __str__(self):
        return u'{0}'.format(self.severity)
    

class Component(models.Model):
    
    Fixed_Asset_Management             ='Fixed Asset Management'
    Payable_Management                 ='Payable Management'
    Procurement_Management             ='Procurement Management'
    Component_Maintenance              ='Component Maintenance'
    Receivables_Management             ='Receivables Management'
    Finance_Setup                      ='Finance Setup'
    Book_Keeping                       ='Book Keeping'
    Inventory_Setup                    ='Inventory Setup'
    Configuration_Management           ='Configuration Management'
    Engineering_Change_Management      ='Engineering Change Management'
    Hangar_Maintenance                 ='Hangar Maintenance'
    Integration                        ='Integration'
    Inventory_Setup                    ='INV'
    Line_Maintenance                   ='Line Maintenance'
    Management_Accounting              ='Management Accounting'
    Material_Request                   ='Material Request'
    Service_Sales_Management           ='Service Sales Management '
    Flight_Billing                     ='Flight Billing'
    
    
    
    
    BPC_ALL =((Fixed_Asset_Management, 'Fixed Assets Management'),
          (Payable_Management,'Payable Management'),
          (Procurement_Management,'Procurement Management'),
          (Component_Maintenance,'Component Maintenance'),
          (Receivables_Management,'Receivables Management'),
          (Finance_Setup,'Finance Setup'),
          (Book_Keeping ,'Book Keeping'),
          (Inventory_Setup,'Inventory Setup'),
          (Configuration_Management,'Configuration Management'),
          (Engineering_Change_Management,'Engineering Change Management'),
          (Hangar_Maintenance ,'Hangar Maintenance'),
          (Integration,'Integration'),
          (Inventory_Setup,'Inventory Setup'),
          (Line_Maintenance,'Line Maintenance'),
          (Management_Accounting,'Management Accounting'),
          (Material_Request,'Material Request'),
          (Service_Sales_Management,'Service Sales Management'),
          (Flight_Billing  ,'Flight Billing'))
              
              
           
          
    bpc=models.CharField("BPC",primary_key=True,max_length=100,choices=BPC_ALL)
    bpc_code=models.CharField("BPC Code",max_length=20,blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Business Components'
        db_table='dhm_bpc'


    def __str__(self):
        return u'{0}'.format(self.bpc)


class Modules(models.Model):
    Maintenance ='Maintenance'
    Material= 'Material'
    Sales='Sales'
    Finance='Finance'
    TEAM_ALL=((Maintenance,'Maintenance'),
         (Material,'Materials'),
         (Sales,'Sales'),
         (Finance,'Finance'))

    module=models.CharField("Module Name",primary_key=True,max_length=40,choices=TEAM_ALL)
    seq=models.CharField("Sequence No.",max_length=50,blank=True)

    class Meta:
        verbose_name_plural = 'Module'
        db_table='dhm_module'
 

    def __str__(self):
        return u'{0}'.format(self.module)   


class Status(models.Model):
    Active = 'Active'
    Inactive = 'Inactive'
    Both = 'Both active and inactive'
    STATUS_ALL=((Active,'Active'),
                (Inactive,'Inactive'),
                (Both, 'Both active and inactive'))
    sp_status=models.CharField("SP Status",primary_key=True,max_length=30,choices=STATUS_ALL)

    class Meta:
        verbose_name_plural= 'SP Status'
        db_table='dhm_sp_status'
        
    def __str__(self):
        return u'{0}'.format(self.sp_status) 
        
   

    
   

    
    
                                
            
       
