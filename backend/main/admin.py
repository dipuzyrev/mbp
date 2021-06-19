from django.contrib import admin
from .models import *

class ShowId(admin.ModelAdmin):
    readonly_fields = ['id']

admin.site.register(User, ShowId)
admin.site.register(Measurement, ShowId)
admin.site.register(Treatment, ShowId)
admin.site.register(Notes, ShowId)
admin.site.register(Tonometer, ShowId)