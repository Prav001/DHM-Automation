from django.contrib import admin

from consistency.models import DHM_Consis_Repository


class ConsisRepoAdmin(admin.ModelAdmin):
    search_fields=('Query_Title',)
    list_display=('Query_Title',)



admin.site.register(DHM_Consis_Repository,ConsisRepoAdmin)
