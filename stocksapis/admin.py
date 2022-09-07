from django.contrib import admin
from .models import Company
from . import models


# @admin.register(models.Company)
# class CompanyAdmin(admin.ModelAdmin):
  
#     list_display = ['company_name', 'opening',
#                     'closing', 'volume']
    # list_editable = ['company_name']
    # list_filter = ['company_name', 'opening',
    #                 'closing', 'volume']
    # list_per_page = 10
    # list_select_related = ['collection']
    # search_fields = ['company_name']