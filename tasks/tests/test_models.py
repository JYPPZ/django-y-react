from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='TesterUser', password='p4ssw0rd123')
        cls.task = Task.objects.create(
            user=cls.user,
            title='Prueba de Modelo',
            description='Una descripción de prueba.'
        )

    def test_title_content(self):
        """Prueba que el título de la tarea es correcto."""
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, 'Prueba de Modelo')

    def test_task_str_representation(self):
        """Prueba la representación en string del modelo."""
        task = Task.objects.get(id=self.task.id)
        # El método __str__ debe devolver el título
        self.assertEqual(str(task), task.title)

    def test_task_is_assigned_to_user(self):
        """Prueba que la tarea está correctamente asignada a un usuario."""
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.user, self.user)

    def test_default_completed_status_is_false(self):
        """Prueba que una nueva tarea no está completada por defecto."""
        task = Task.objects.get(id=self.task.id)
        self.assertFalse(task.completed)