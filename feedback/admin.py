from django.contrib import admin
from .models import Feedback
from django.http import HttpResponse
import csv

# Register your models here.


def export_feedbacks(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="feedbacks.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Message', 'Date', 'Time'])
    feedbacks = queryset.values_list(
        'name', 'email', 'phone', 'message', 'date', 'time')
    for feedback in feedbacks:
        writer.writerow(feedback)
    return response


export_feedbacks.short_description = 'Export as csv'


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date', 'time')
    ordering = ('name', 'email', 'phone', 'message', 'date', 'time')
    search_fields = ('name', 'email', 'phone', 'message', 'date', 'time')
    list_filter = ['name', 'date']
    sortable_by = ['name']
    actions = [export_feedbacks]


admin.site.register(Feedback, PageAdmin)
