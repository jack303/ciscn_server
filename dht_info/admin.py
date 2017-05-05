from django.contrib import admin
from .models import DhtResource
# Register your models here.

class DhtResourceAdmin(admin.ModelAdmin):
    pass

admin.site.register(DhtResource,DhtResourceAdmin)