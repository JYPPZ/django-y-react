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
        Define dinámicamente el queryset basado en la acción.
        - Para 'list', solo devuelve las tareas del usuario.
        - Para acciones de detalle, devuelve todas las tareas para que los permisos puedan actuar.
        """
        if self.action == 'list':
            # Para la lista, filtramos por usuario y optimizamos.
            return Task.objects.filter(user=self.request.user).select_related('user').order_by('-created_at') # evitar N+1
        
        # Para 'retrieve', 'update', 'destroy', etc., empezamos con todas las tareas,
        # para verificar si el request.user es el dueño del objeto encontrado.
        return Task.objects.all().select_related('user')

    def perform_create(self, serializer):
        """
        Asigna automáticamente el usuario autenticado a la tarea al crearla.
        """
        serializer.save(user=self.request.user)