from rest_framework import serializers
from .models import EventPayment, EventRefund, EventSettlement

class EventPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPayment
        fields = '__all__'

class EventRefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRefund
        fields = '__all__'

class EventSettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSettlement
        fields = '__all__'