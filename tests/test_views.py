from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APIRequestFactory
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView
from restaurant.models import Menu
from django.test import Client

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = Client()
        Menu(title="Cake", price=21, inventory=5).save()
        Menu(title="Candy", price=45, inventory=3).save()
    
    def test_view_response(self):
        request = self.factory.get('/restaurant/menu/')
        request.user = AnonymousUser()
        response = MenuItemView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    def test_get_all(self):        
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)