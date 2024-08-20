from rest_framework import viewsets
from .models import EventPayment, EventRefund
from .serializers import EventPaymentSerializer, EventRefundSerializer

class EventPaymentViewSet(viewsets.ModelViewSet):
    queryset = EventPayment.objects.all()
    serializer_class = EventPaymentSerializer

class EventRefundViewSet(viewsets.ModelViewSet):
    queryset = EventRefund.objects.all()
    serializer_class = EventRefundSerializer