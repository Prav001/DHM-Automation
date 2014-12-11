import django_tables2 as tables
from consistency.models import DHM_Consis_Repository,DHM_Consis_Report


class ConsisTable(tables.Table):
    
    class Meta:
        model=DHM_Consis_Repository
        exclude = ("Component_Code","Consistency_CheckType","QueryText_SpName","id",)
        sequence = ("Query_Title","BPC_Name","...")
        order_by=  ("BPC_Name")
        
class ConsisReport(tables.Table):

    class Meta:
        model=DHM_Consis_Report
        exclude=("con_guid","id",)
        #order_by=("con_rundate")
