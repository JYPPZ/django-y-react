from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Task.
    """
    # Mostrar el nombre del usuario, no solo su ID
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'user']
        read_only_fields = ['created_at', 'user']

    # --- Validación Personalizada ---
    # DRF buscará métodos que comiencen con 'validate_<nombre_del_campo>'
    def validate_title(self, value):
        """
        Añade una validación personalizada para el campo 'title'.
        Asegura que el título tenga al menos 3 caracteres.
        """
        if len(value) < 3:
            raise serializers.ValidationError("El título debe tener al menos 3 caracteres.")
        return value