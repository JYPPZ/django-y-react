from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    """
    Endpoint para el registro de nuevos usuarios.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer