from django.apps import AppConfig
from django.db.models.signals import post_save,pre_save





class ProfilesConfig(AppConfig):
    name = 'profiles'
    
    def ready(self):
        from django.contrib.auth import get_user_model
        from .signals import create_profile
        User= get_user_model()
        post_save.connect(create_profile,sender=User)