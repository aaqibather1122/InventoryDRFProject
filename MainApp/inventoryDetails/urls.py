from django.urls import path

from .views import InventoryCheckView, InventoryList, InventoryEdit

urlpatterns = [
    path('inventory/',InventoryList.as_view(),name ='inventory_list'),
    path('inventory/check/<int:product_id>/', InventoryCheckView.as_view(), name='inventory_check'),
    path('inventoryEdit/<int:product_id>',InventoryEdit.as_view(),name ='inventory_edit'),
]

