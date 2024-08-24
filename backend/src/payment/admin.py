from django.contrib import admin

# Register your models here.
from .models import EventPayment, EventRefund, EventSettlement 

admin.site.register(EventPayment)
admin.site.register(EventRefund)
admin.site.register(EventSettlement)