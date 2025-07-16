from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    # Título da tarefa (obrigatório, máximo 200 caracteres)
    title = models.CharField(max_length=200)
    
    # Descrição da tarefa (opcional, pode ficar vazio)
    description = models.TextField(blank=True)
    
    # Se a tarefa está concluída (padrão: False = não concluída)
    completed = models.BooleanField(default=False)
    
    # Data de criação (preenchida automaticamente quando criar)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Usuário dono da tarefa (cada tarefa pertence a um usuário)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Como o objeto aparece quando impresso (ex: no admin)
    def __str__(self):
        return self.title
    
    # Configurações do modelo
    class Meta:
        ordering = ['-created_at']  # Mais recentes primeiro

