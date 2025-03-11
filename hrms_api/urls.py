from django.urls import include, path

urlpatterns = [
    path("auth/", include("hrms_api.api_urls.auth.urls")),
    path("asset/", include("hrms_api.api_urls.asset.urls")),
    path("base/", include("hrms_api.api_urls.base.urls")),
    path("employee/", include("hrms_api.api_urls.employee.urls")),
    path("notifications/", include("hrms_api.api_urls.notifications.urls")),
    path("payroll/", include("hrms_api.api_urls.payroll.urls")),
    path("attendance/", include("hrms_api.api_urls.attendance.urls")),
    path("leave/", include("hrms_api.api_urls.leave.urls")),
]
