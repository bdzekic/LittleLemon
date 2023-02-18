from django.urls import path
from . import views

urlpatterns = [
    #path('Menuitems/',views.Menuitems)
    path('menu-items/',views.MenuItemView.as_view()),
    path('menu-items/<int:pk>',views.SingleMenuItemView.as_view()),
    path('cart/menu-items/',views.CartView.as_view()),
    path('orders/',views.OrderView.as_view()),
    path('orders/<int:pk>',views.SingleOrderView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('manager/users',views.ManagerView.as_view())
    
]