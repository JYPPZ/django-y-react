from rest_framework import viewsets, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los usuarios ver, crear, editar o eliminar sus propias tareas.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']  # Permite filtrar por el campo 'completed'
    search_fields = ['title', 'description'] # Permite búsqueda de texto en title y description
    ordering_fields = ['created_at', 'title'] # Permite ordenar por estos campos

    def get_queryset(self):
        """
        Esta vista debe devolver una lista de todas las tareas
        para el usuario actualmente autenticado, optimizada.
        """
        user = self.request.user
        return user.tasks.select_related('user').all().order_by('-created_at') # Evitar N+1

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado a la tarea al crearla.
        """
        serializer.save(user=self.request.user)