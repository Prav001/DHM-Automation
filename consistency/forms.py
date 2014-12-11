from django import forms
from django.utils.safestring import mark_safe
from django.db import models
from django.forms import ModelChoiceField
import re
import datetime
from django.utils import timezone
from django.forms.fields import DateField
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms.extras import SelectDateWidget
from masters.models import Customer,Modules,Component,Criticality
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ConsistencyForm(forms.Form):
    Customer=forms.ModelChoiceField(
        label="Customer Name",
        widget=forms.Select,
        queryset=Customer.objects.all(),
        empty_label=None,
        )

    Severity_level=forms.ModelChoiceField(
        label="Severity Level",
        widget=forms.Select,
        queryset=Criticality.objects.all(),
        empty_label=None
        )
    
    run_date=forms.DateField(
        label="Run Date",
        widget=SelectDateWidget(years=range(2000, datetime.date.today().year+1)),initial=timezone.now(),
        help_text='</br> ')
        
##    run_date=forms.DateField(
##        label="Run Date",
##        widget=forms.TextInput(attrs=
##                                {
##                                    'class':'datepicker'
##                                }))
    
    
    min_count=forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'size':7,'placeholder':'Min. query count ',}),
        label ="Inc. record min# "
        )

    desc_like = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Type SP description',}),
        help_text='</br>'
        )
     
    Modules=forms.ModelMultipleChoiceField(
         label="Business Module",
        widget=forms.CheckboxSelectMultiple,
        queryset=Modules.objects.all(),error_messages={'required': 'Choose atleast one of the Modules'},
        )
    
    Components=forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Component.objects.all(),error_messages={'required': 'Choose atleast one of the Components'},
        )
    
    

    


    
    
   
