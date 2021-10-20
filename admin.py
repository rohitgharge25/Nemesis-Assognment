from django.contrib import admin

from .models import database


@admin.register(database)
class database_user(admin.ModelAdmin):
    list_display = ('user_name','first_name','last_name','Email','password')
