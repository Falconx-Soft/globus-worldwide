from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
# from import_export import ImportExportModelAdmin
# Register your models here.

class WarehouseResource(resources.ModelResource):

    class Meta:
        model = ware_house_model
class WareouseAdmin(ImportExportModelAdmin):
    # list_display= ("customer_name","customer_id", "serial_number","height","width","length", "storage_space", "weight", "storage_name", "locate", "date", "description", "quantity", "warehouse" )
     pass

admin.site.register(ware_house_model, WareouseAdmin)