from django.apps import AppConfig


class CommanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.comman'

    def ready(self):
        import apps.comman.signals
