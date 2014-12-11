from django import forms
from masters.models import Customer
from django.contrib import admin
import datetime
from django.utils import timezone
from django.forms.fields import DateField
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms.extras import SelectDateWidget


class TranForm(forms.Form):
    customer_name=forms.ModelChoiceField(
        label="Customer Name",
        widget=forms.Select,
        queryset=Customer.objects.all(),
        empty_label=None,
        help_text='</br>')
    
    fromdate = forms.DateField(label="From Date", widget=SelectDateWidget(years=range(2000, datetime.date.today().year+10)),initial=timezone.now(),help_text='</br>')
    todate = forms.DateField(label="To Date", widget=SelectDateWidget(years=range(2000,datetime.date.today().year+10)),initial=timezone.now())
    
   
