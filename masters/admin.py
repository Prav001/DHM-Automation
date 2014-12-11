from django.contrib import admin

# Register your models here.
from masters.models import Customer,Criticality,Component,Modules

class CustomerAdmin(admin.ModelAdmin):
    search_fields=('cust_name',)
    list_display=('cust_name',)


class CriticalityAdmin(admin.ModelAdmin):
    list_display=('severity',)
    search_fields=('severity',)


class ComponentAdmin(admin.ModelAdmin):
    list_display=('bpc',)
    list_filter=('bpc',)
    search_fields=('bpc',)



class ModulesAdmin(admin.ModelAdmin):
    list_display=('module',)
    list_filter=('module',)
    search_fields=('module',)


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Criticality,CriticalityAdmin)
admin.site.register(Component,ComponentAdmin)
admin.site.register(Modules,ModulesAdmin) 

    
    
    
    
    
    
