from rest_framework import serializers
from payments.models import Payment

from products.serializers import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Payment
        fields = '__all__'