from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError

class TranStats(models.Model):

    BPC =models.CharField(max_length=200)
    tran_date=models.DateField()
    tran_desc=models.CharField(max_length=800)
    status=models.CharField(max_length=200)
    count=models.IntegerField()

    class Meta:
        verbose_name_plural = 'Transactions Statistics'
        db_table='cust_tran_stats_tbl'
    
    def __str__(self):
        return u'{0}'.format(self.tran_date)



    
    
