from django.contrib import admin

# Register your models here.
from .models import EventPayment, EventRefund

admin.site.register(EventPayment)
admin.site.register(EventRefund)