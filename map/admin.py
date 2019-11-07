from django.contrib import admin

# Register your models here.
from map.models import Answer, Map



class AnswersAdmin(admin.ModelAdmin):
    list_filter = ['timecode']
    search_fields = ['group']
    list_display = ('__str__', 'group', 'timecode', 'correct', 'map')


admin.site.register(Map)
# admin.site.register(Hrono)
admin.site.register(Answer, AnswersAdmin)
