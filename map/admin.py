from django.contrib import admin

# Register your models here.
from map.models import Answer, Map

admin.site.register(Map)
# admin.site.register(Hrono)
admin.site.register(Answer)
