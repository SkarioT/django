from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Profile)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class ProfileInline(admin.StackedInline):
#     model = models.Profile
#     can_delete = False
#     verbose_name_plural = 'Профиль'

# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
