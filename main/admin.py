from django.contrib import admin
from .models import Manager, News, Categoryq


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
   list_display = ['user']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
   list_display = ['title', 'manager']

@admin.register(Categoryq)
class CategoryqAdmin(admin.ModelAdmin):
   list_display = ['category_name', 'title']