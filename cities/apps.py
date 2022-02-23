from django.apps import AppConfig


class CitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cities'
    # Для отображения в админке.
    verbose_name = 'Приложение Города'
