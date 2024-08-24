from rest_framework import viewsets
from .models import EventPayment, EventRefund, EventSettlement
from .serializers import EventPaymentSerializer, EventRefundSerializer, EventSettlementSerializer

class EventPaymentViewSet(viewsets.ModelViewSet):
    queryset = EventPayment.objects.all()
    serializer_class = EventPaymentSerializer

class EventRefundViewSet(viewsets.ModelViewSet):
    queryset = EventRefund.objects.all()
    serializer_class = EventRefundSerializer

class EventSettlementViewSet(viewsets.ModelViewSet):
    queryset = EventSettlement.objects.all()
    serializer_class = EventSettlementSerializer