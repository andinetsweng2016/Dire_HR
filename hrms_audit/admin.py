"""
admin.py
"""

from django.contrib import admin

from hrms_audit.models import AuditTag, HrmsAuditInfo, HrmsAuditLog

# Register your models here.

admin.site.register(AuditTag)
