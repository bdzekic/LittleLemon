from rest_framework import serializers
from .models import MenuItem,Cart,Category,Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id' ,'title' ]


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = [ 'id','title'  ,'price' , 'featured' , 'category','category_id']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [ 'user' ,'menuitem' , 'quantity', 'unit_price', 'price']
        
  
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [ 'order' , 'menuitem' ,'quantity', 'unit_price' , 'price' ]     