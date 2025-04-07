from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Product)
class PoductAdmin(admin.ModelAdmin):
    list_display = ['title','price','inventory_status','collection']
    list_per_page=10
    @admin.display(ordering='inventoey')
    def inventory_status(self,product):
        if product.inventoey < 10:
            return 'Low'
        return 'hight'
admin.site.register(models.Collection)
