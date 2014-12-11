from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Graphs(models.Model):
    
      cust_name=models.CharField("Customer",max_length=100,blank=False)
      module_name=models.CharField("Module",max_length=100,blank=False)
      bpc_name=models.CharField("BPC",max_length=100,blank=True)
      rundate=models.DateField("Run Date",max_length=100,blank=False)
      total_count=models.IntegerField("Total Count",primary_key=True,blank=True,default=0)
      bpc_count=models.IntegerField("BPCwise Count",blank=True,default=0)
      module_count=models.IntegerField("Modulewise Count",blank=True,default=0)
      


      class Meta:
         verbose_name_plural = 'Graph Database'
         db_table='dhm_graph_tbl'

      def __str__(self):
        return u'{0}'.format(self.total_count)    
     
   


      
        
       

     



     
