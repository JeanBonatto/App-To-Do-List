from django.shortcuts import render
from .models import Todo

def todo_list(request):
    """
    View que mostra a lista de todas as tarefas
    """
    # Busca todas as tarefas do banco de dados
    todos = Todo.objects.all()
    
    # Conta quantas tarefas estão concluídas e pendentes
    completed_count = todos.filter(completed=True).count()
    pending_count = todos.filter(completed=False).count()
    
    # Dados que vamos enviar para o template
    context = {
        'todos': todos,
        'completed_count': completed_count,
        'pending_count': pending_count,
    }
    
    # Renderiza o template com os dados
    return render(request, 'todos/todo_list.html', context)
