from django.apps import AppConfig


class MiappConfig(AppConfig):
    name = 'miapp'

    def ready(self):
        import miapp.signals