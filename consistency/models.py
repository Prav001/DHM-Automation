from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError



class DHM_Consis_Repository(models.Model):
    Active = 'Active'
    Inactive   = 'Inactive'
    STATUS_ALL=((Active,'Active'),
                (Inactive,'Inactive'))
    
    BPC_ShortCode=models.CharField(verbose_name='BPC Code',max_length=100)
    Query_Title=models.CharField(max_length=2000)
    BPC_Name=models.CharField(verbose_name='BPC',max_length=100)
    Component_Code=models.CharField(max_length=100)
    Title_Description=models.CharField(verbose_name='Description',max_length=2000)
    Consistency_CheckType=models.CharField(max_length=500)
    QueryText_SpName=models.CharField(max_length=200)
    Criticality=models.CharField(max_length=100)
    status=models.CharField("SP Status",max_length=30,choices=STATUS_ALL,blank=True)


    class Meta:
        verbose_name_plural = 'Consistency Repository'
        db_table='DHM_Consis_Repository'
    
    def __str__(self):
        return u'{0}'.format(self.Query_Title)


class DHM_Consis_Report(models.Model):
    FRESH = 'Fresh/New'
    OLD   = 'Old'
    STATUS_ALL=((FRESH,'Fresh/New'),
                (OLD,'Old'))
    con_guid=models.CharField(verbose_name='GUID',max_length=200)
    conquery_source=models.CharField(verbose_name='Customer ',max_length=50)
    con_sno=models.IntegerField(verbose_name='Serial No.')
    conquery_name=models.CharField(verbose_name='Query Name ',max_length=100)
    conquery_count=models.IntegerField(verbose_name='Count')
    conquery_desc=models.CharField(verbose_name='Query Description',max_length=300,blank=True)
    bpc_name=models.CharField(verbose_name='BPC',max_length=300,blank=True)
    criticality=models.CharField(verbose_name='Criticality',max_length=50,blank=True)
    sp_status=models.CharField("SP Status",max_length=30,choices=STATUS_ALL)
    con_rundate=models.DateField(verbose_name='RunDate',blank=True)
    instance_id=models.IntegerField(verbose_name='Run #')


    class Meta:
        verbose_name_plural='Consistency Report Table'
        db_table='dhm_consis_report_tbl'
    
    def __str__(self):
        return u'{0}'.format(self.conquery_count)
