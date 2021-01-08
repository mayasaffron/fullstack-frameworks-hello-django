from django.test import TestCase
from .models import item
# Create your tests here.


class TestViews(TestCase):
    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        list_item = item.objects.create(name='Test todo edit')
        response = self.client.get(f'/edit/{list_item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')
    
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test added item'})
        self.assertRedirects(response, '/')
    
    def test_can_delete_item(self):
        list_item = item.objects.create(name='Test todo delete')
        response = self.client.get(f'/delete/{list_item.id}')
        self.assertRedirects(response, '/')
        existing_item = item.objects.filter(id=list_item.id)
        self.assertEqual(len(existing_item), 0)

    def test_can_toggle_item(self):
        list_item = item.objects.create(name='Test todo toggle', status=True)
        response = self.client.get(f'/toggle/{list_item.id}')
        self.assertRedirects(response, '/')
        updated_item = item.objects.get(id=list_item.id)
        self.assertFalse(updated_item.status)

    def test_can_edit_item(self):
        list_item = item.objects.create(name='Test todo edit')
        response = self.client.post(f'/edit/{list_item.id}',
                                   {'name': 'new name'})
        self.assertRedirects(response, '/')
        updated_item = item.objects.get(id=list_item.id)
        self.assertEqual(updated_item.name, 'new name')
