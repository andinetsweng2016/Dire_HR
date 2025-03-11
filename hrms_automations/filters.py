"""
hrms_automations/filters.py
"""

from hrms.filters import HrmsFilterSet, django_filters
from hrms_automations.models import MailAutomation


class AutomationFilter(HrmsFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
