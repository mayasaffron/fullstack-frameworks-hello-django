from django.test import TestCase
from .models import item
# Create your tests here.


class TestModels(TestCase):
    def test_status_is_false_by_default(self):
        list_item = item.objects.create(name='Test todo status')
        self.assertFalse(list_item.status)

    def test_item_string_method_returns_name(self):
        test_item = item.objects.create(name='Test todo Item')
        self.assertEqual(str(test_item), 'Test todo Item')
