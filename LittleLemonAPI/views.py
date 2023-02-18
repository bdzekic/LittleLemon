from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem,Cart,Category,Order
from .serializers import MenuItemSerializer,CartSerializer,CategorySerializer,OrderSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User,Group



#Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    ordering_fields = ['price']
    filterset_fields = ['price']
    search_fields = ['title']
    
    def get_permissions(self):
     if(self.request.method=='GET'):
        return []

     return [IsAuthenticated()]
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class=CartSerializer
    
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer
    
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer

class SingleOrderView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderSerializer
    
#@api_view()
#@permission_classes()
class ManagerView(generics.ListCreateAPIView):
  #if User.groups.filter(name='Manager').exist():
    def get_permissions(self):
        
     if(self.group.filter =='manager'):
        return []
     return [IsAuthenticated()]