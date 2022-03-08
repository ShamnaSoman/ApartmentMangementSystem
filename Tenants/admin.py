from django.contrib import admin
from .models import Tenants , User ,Visitor ,Complaints

# Register your models here.
admin.site.register(Tenants)
admin.site.register(User)
admin.site.register(Visitor)
admin.site.register(Complaints)