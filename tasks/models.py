from django.db import models
from django.conf import settings

class Task(models.Model):
    # Cada tarea pertenece a un usuario
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    # Título de la tarea (obligatorio)
    title = models.CharField(max_length=200)
    # Descripción de la tarea (opcional)
    description = models.TextField(blank=True, null=True)
    # Estado de la tarea (completada o no)
    completed = models.BooleanField(default=False)
    # Fecha de creación (se establece automáticamente al crear el objeto)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title