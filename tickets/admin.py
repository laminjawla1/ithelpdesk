from django.contrib import admin
from .models import Ticket, Expert, Specialization
from django.http import HttpResponse
import csv


# Register your models here.
def export_tickets(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tickets.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Phone', 'Issue',
                    'Category', 'Status', 'Cycle', 'Assigned To', 'Date', 'Time'])
    tickets = queryset.values_list(
        'name', 'phone', 'issue',
        'category', 'status', 'cycle', 'assigned_to', 'date', 'time')
    for ticket in tickets:
        writer.writerow(ticket)
    return response


export_tickets.short_description = 'Export as csv'


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'issue',
                    'category', 'status', 'cycle', 'date', 'time')
    ordering = ('name', 'phone', 'issue',
                'category', 'status', 'cycle', 'date', 'time')
    search_fields = ('name', 'phone', 'issue',
                     'category', 'status', 'cycle', 'date', 'time')
    list_filter = ['name', 'issue',
                   'category', 'status', 'cycle', 'assigned_to', 'date']

    fieldsets = (
        ('Meta Information', {
            'classes': ('collapse',),
            'fields': ('name', 'issue', 'description', 'date', 'time')
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('phone', 'anydesk', 'zone', 'branch')
        }),
        ('Ticket Information', {
            'classes': ('collapse',),
            'fields': ('category', 'cycle', 'status', 'image', 'date_closed', 'documentation')
        }),
        ('Ticket Admin', {
            'classes': ('collapse',),
            'fields': ('assigned_to', 'verification')
        }),
    )
    actions = [export_tickets]


class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',
                    'phone', 'level')
    ordering = ('name', 'address',
                'phone', 'email', 'specialization', 'level')
    search_fields = ('name', 'address',
                     'phone', 'email', 'specialization', 'level')
    list_filter = ['name', 'address',
                   'phone', 'email', 'specialization', 'level']
    sortable_by = ['name', 'specialization']


admin.site.register(Ticket, PageAdmin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Specialization)
