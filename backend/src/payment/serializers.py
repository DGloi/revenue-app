from rest_framework import serializers
from .models import EventPayment, EventRefund

class EventPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPayment
        fields = '__all__'

class EventRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRefund
        fields = '__all__'