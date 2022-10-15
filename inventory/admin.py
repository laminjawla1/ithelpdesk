from .models import Inventory
from django.http import HttpResponse
from django.contrib import admin
from .models import Inventory
import csv
# Register your models here.


def export_assets(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assets.csv"'
    writer = csv.writer(response)
    writer.writerow(['Model', 'Category', 'Serial Number',
                    'Location', 'User Name', 'Status', 'Date'])
    assets = queryset.values_list(
        'model', 'category', 'serial_number',
        'location', 'user_name', 'status', 'date')
    for asset in assets:
        writer.writerow(asset)
    return response


def import_assets(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assets.csv"'
    reader = csv.reader(response)
    reader.readrow(['Model', 'Category', 'Serial Number',
                    'Location', 'User Name', 'Status', 'Date'])
    assets = queryset.values_list(
        'model', 'category', 'serial_number',
        'location', 'user_name', 'status', 'date')
    for asset in assets:
        reader.readrow(asset)
    return response


export_assets.short_description = 'Export as csv'
import_assets.short_description = 'Import csv'


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('model', 'category', 'serial_number',
                    'location', 'user_name', 'status', 'date')
    ordering = ('model', 'category', 'serial_number',
                'location', 'user_name', 'status', 'date')
    search_fields = ('model', 'category', 'serial_number',
                     'location', 'user_name', 'status', 'date')
    list_filter = ('model', 'category', 'serial_number',
                   'location', 'user_name', 'status', 'date')
    sortable_by = ['name']
    actions = [export_assets, import_assets]


admin.site.register(Inventory, InventoryAdmin)
