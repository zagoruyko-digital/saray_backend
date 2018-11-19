from django.contrib import admin
from .models import Manager, News


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
   list_display = ['user']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
   list_display = ['title', 'manager']