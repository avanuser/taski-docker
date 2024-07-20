"""Apps for API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Api config for API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
