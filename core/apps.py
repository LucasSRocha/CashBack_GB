from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "core"

    def ready(self):
        # noinspection PyUnresolvedReferences
        import core.signals
