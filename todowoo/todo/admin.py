from django.contrib import admin
from . import models


@admin.register(models.Todos)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'important', 'completed', 'user']
    list_editable = ['important', 'completed']
    list_per_page = 10
    list_select_related = ['user']
