import re
import datetime

from django import forms
from masters.models import all


class MetaForm(forms.Form):
    customer=forms.ModelChoiceField(empty_label=None, widget=forms.HiddenInput())
    criticality=forms.ModelChoiceField(empty_label=None, widget=forms.HiddenInput())
    components=forms.ModelChoiceField(empty_label=None, widget=forms.HiddenInput())
    team=forms.ModelChoiceField(empty_label=None, widget=forms.HiddenInput())

    
                                     

    
    
