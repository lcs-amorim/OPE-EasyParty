from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from core.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["codigo_u","nome_u","usuario","senha","email_u","cpf","telefone_u","endereco_u","news"]
    search_fields = ["nome_u","usuario","cpf","email_u"]
    filter_horizontal = []
    ordering = ["codigo_u"]
    list_filter = []

admin.site.register(Usuario,UsuarioAdmin)