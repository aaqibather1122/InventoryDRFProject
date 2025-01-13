
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userrole.urls')),
    path('',include('customer.urls')),
    path('',include('supplier.urls')),
    path('',include('company.urls')),
    path('',include('product.urls')),
    path('',include('inventoryDetails.urls')),
    path('',include('order.urls')),
    # path('',include('orderdetail.urls')),
]
