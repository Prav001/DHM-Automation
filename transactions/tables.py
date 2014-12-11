import django_tables2 as tables
from transactions.models import TranStats


class Trantable(tables.Table):
    BPC=tables.Column()
    tran_date=tables.Column(verbose_name='transaction date')
    tran_desc=tables.Column(verbose_name='transaction details')
    status=tables.Column()
    count=tables.Column()
    
    class Meta:
        model=TranStats
        exclude=("id",)
