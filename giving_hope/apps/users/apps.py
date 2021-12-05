from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'giving_hope.apps.users'

    def ready(self):
        import giving_hope.apps.users.signals
