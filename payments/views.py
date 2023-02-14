from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from payments.models import Payment

from payments.serializers import PaymentSerializer
# Create your views here.

class PaymentView(ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Payment.objects.filter(order__user = self.request.user)
        return queryset
