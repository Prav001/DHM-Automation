from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
from masters.models import all 

def result(request):
    form=MetaForm()
    if request.method == "POST":
        form=MetaForm(request.POST)
        if form.is_valid:
            return HttpResponseRedirect('http://172.26.5.64:8000/')
    errors = form.errors or None # form not submitted or it has errors
    return render(request, 'masters/meta.html',{
          'form': form,
          'errors': errors,
   })                        
        
