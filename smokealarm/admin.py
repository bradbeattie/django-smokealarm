from django.contrib import admin
from smokealarm.models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ["error", "owner", "created"]
    list_filter = ["created"]
    ordering = ["-created"]
    search_fields = ["error", "file", "line", "url", "additional_data"]
admin.site.register(Report, ReportAdmin)
