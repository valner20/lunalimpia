from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Profesional, Cliente, Turno




@admin.register(Turno)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'profesional', 'fecha', 'hora',)
    list_filter = ('fecha', 'profesional',)
    search_fields = (
    'cliente__nombre',
    'profesional__username',)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')

@admin.register(Profesional)
class ProfesionalAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets
