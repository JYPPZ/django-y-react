from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner 

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los usuarios ver, crear, editar o eliminar sus propias tareas.
    """
    serializer_class = TaskSerializer
    
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Devuelve todas las tareas del usuario autenticado.
        """
        return self.request.user.tasks.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado a la tarea al crearla.
        """
        serializer.save(user=self.request.user)