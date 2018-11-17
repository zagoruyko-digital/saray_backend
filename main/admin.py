from django.contrib import admin
from .models import Manager


@admin.register(Manager)
class Managerdmin(admin.ModelAdmin):
   list_display = ['user']