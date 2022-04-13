from django.apps import AppConfig

class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'
    verbose_name = 'Мониторинг'

    def ready(self) -> None:
        from tracker import pulling
        pulling.start()
