from django.shortcuts import render

# views.py
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment.serializer import PaymentIntentSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntentView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PaymentIntentSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data['amount']
            currency = serializer.validated_data['currency']

            try:
                payment_intent = stripe.PaymentIntent.create(
                    amount=int(amount * 100),
                    currency=currency,
                    payment_method_types=['card'],
                )

                return Response({
                    'message': 'Payment Intent created successfully',
                    'transaction_id': payment_intent['id'],
                    'amount': amount,
                    'currency': currency
                }, status=status.HTTP_201_CREATED)

            except stripe.error.StripeError as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

