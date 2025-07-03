from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear dos usuarios para probar los permisos
        cls.user1 = User.objects.create_user(username='user1', password='p4ssw0rd123')
        cls.user2 = User.objects.create_user(username='user2', password='p4ssw0rd123')

        # Crear tareas, una para cada usuario
        cls.task1 = Task.objects.create(user=cls.user1, title='Tarea de User1')
        cls.task2 = Task.objects.create(user=cls.user2, title='Tarea de User2')
    
    def test_create_task_authenticated(self):
        """Prueba que un usuario autenticado puede crear una tarea."""
        self.client.force_authenticate(user=self.user1)
        url = reverse('task-list')  # 'task-list' es el nombre que el router de DRF le da a esta ruta
        data = {'title': 'Nueva Tarea desde Prueba'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3) # Ahora hay 3 tareas en total
        self.assertEqual(Task.objects.last().title, 'Nueva Tarea desde Prueba')
        self.assertEqual(Task.objects.last().user, self.user1)

    def test_create_task_unauthenticated(self):
        """Prueba que un usuario no autenticado no puede crear una tarea."""
        url = reverse('task-list')
        data = {'title': 'Tarea no permitida'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_own_tasks(self):
        """Prueba que un usuario solo puede listar sus propias tareas."""
        self.client.force_authenticate(user=self.user1)
        url = reverse('task-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # La paginación devuelve los resultados en 'results' y el conteo en 'count'
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], self.task1.title)

    def test_user_cannot_update_another_users_task(self):
        """Prueba que un usuario no puede actualizar la tarea de otro."""
        self.client.force_authenticate(user=self.user1)
        url = reverse('task-detail', kwargs={'pk': self.task2.id})
        data = {'title': 'Título modificado ilegalmente', 'completed': True}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_user_can_update_own_task(self):
        """Prueba que un usuario puede actualizar su propia tarea."""
        self.client.force_authenticate(user=self.user1)
        url = reverse('task-detail', kwargs={'pk': self.task1.id})
        data = {'title': 'Título actualizado', 'completed': True}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db() # Recargar el objeto desde la BD
        self.assertEqual(self.task1.title, 'Título actualizado')
        self.assertTrue(self.task1.completed)

    def test_user_cannot_delete_another_users_task(self):
        """Prueba que un usuario no puede eliminar la tarea de otro."""
        self.client.force_authenticate(user=self.user1)
        url = reverse('task-detail', kwargs={'pk': self.task2.id})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Task.objects.filter(id=self.task2.id).exists())

    def test_user_can_delete_own_task(self):
        """Prueba que un usuario puede eliminar su propia tarea."""
        self.client.force_authenticate(user=self.user1)
        url = reverse('task-detail', kwargs={'pk': self.task1.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task1.id).exists())