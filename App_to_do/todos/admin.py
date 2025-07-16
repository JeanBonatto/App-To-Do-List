from django.contrib import admin
from .models import Todo

# Registra o modelo Todo no admin
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    # Campos mostrados na lista
    list_display = ['title', 'completed', 'user', 'created_at']
    
    # Filtros na lateral direita
    list_filter = ['completed', 'created_at']
    
    # Campo de busca no topo
    search_fields = ['title', 'description']
    
    # Campos somente leitura (não podem ser editados)
    readonly_fields = ['created_at']
