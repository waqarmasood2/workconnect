from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user', 'path', 'method', 'duration', 'created_at')
    list_filter = ('method', 'user', 'created_at')
    search_fields = ('ip_address', 'path', 'user__username')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'