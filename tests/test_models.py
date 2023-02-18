from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Ice Cream', price=35, inventory=235)
        self.assertEqual(str(item), 'Ice Cream : 35')