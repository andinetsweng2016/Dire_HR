from django.apps import AppConfig


class HrmsApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hrms_api"

    def ready(self):
        from django.urls import include, path

        from hrms.urls import urlpatterns

        urlpatterns.append(
            path("api/", include("hrms_api.urls")),
        )
        super().ready()
