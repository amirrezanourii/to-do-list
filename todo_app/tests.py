from django.test import TestCase
from .models import ToDoList


class ToDoListModelTest(TestCase):
    def setUp(self):
        ToDoList.objects.create(title='test task')

    def test_text_content(self):
        post = ToDoList.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'test task')
