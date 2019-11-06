from django.contrib import admin

# Register your models here.
from map.models import Answer, Map

admin.site.register(Map)
# admin.site.register(Hrono)
admin.site.register(Answer)

# class MyModelAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('js/admin/my_own_admin.js',)
#         css = {
#              'all': ('css/admin/my_own_admin.css',)
#         }