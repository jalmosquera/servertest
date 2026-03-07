from django.contrib import admin
from .models import Pruebas

@admin.register(Pruebas)
class PruebasAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_filter = []
    search_fields = []

