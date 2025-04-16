from django.apps import AppConfig


class AUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_users'
    
    def ready(self):
        import a_users.signals
        # Aqui eu importo o arquivo signals.py, que contém os sinais do Django.
        # Isso é necessário para que os sinais sejam registrados e funcionem corretamente. 
