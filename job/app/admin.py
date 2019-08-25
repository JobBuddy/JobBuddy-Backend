from django.contrib import admin

# Register your models here.
from .models import  companyInfo , recruiters

admin.site.register(companyInfo)
admin.site.register(recruiters)
