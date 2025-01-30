from django.urls import path

from .views import CreatePaymentIntentView

urlpatterns = [
    path('payments/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
]