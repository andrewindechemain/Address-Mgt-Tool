"""This file contains configurations for the tool app
The configuration adds the namaand default_auto_fields fro Db configurations
."""
from django.apps import AppConfig


class ToolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tool'
