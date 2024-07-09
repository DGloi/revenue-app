from django.db import models

# Create your models here.
class EventPayment(models.Model):
    id = models.AutoField(primary_key=True),
    id_payment_gateway_reference = models.CharField(max_length=255)
    id_transaction = models.CharField(max_length=255)
    id_product = models.CharField(max_length=255)
    id_invoice_number = models.CharField(max_length=255)
    amount_net = models.DecimalField(max_digits=10, decimal_places=3)
    amount_discount = models.DecimalField(max_digits=10, decimal_places=3)
    amount_tax = models.DecimalField(max_digits=10, decimal_places=3)
    amount_total = models.DecimalField(max_digits=10, decimal_places=3)
    amount_payment_gateway = models.DecimalField(max_digits=10, decimal_places=3)
    amount_credit = models.DecimalField(max_digits=10, decimal_places=3)
    currency = models.CharField(max_length=3)
    name_payment_gateway = models.CharField(max_length=255)
    country_tax_address = models.CharField(max_length=2)
    country_ip = models.CharField(max_length=2)
    date_invoice = models.DateTimeField()
    date_transaction = models.DateTimeField()
    date_billing_period_start = models.DateTimeField()
    date_billing_period_end = models.DateTimeField()
    name_subscription_description = models.CharField(max_length=255)
    meta_invoice_origin = models.CharField(max_length=255)
    meta_data_origin = models.CharField(max_length=255)
    meta_tax_origin = models.CharField(max_length=255)
    meta_payment_method = models.CharField(max_length=255)
    meta_report_timezone = models.CharField(max_length=255)

    def __str__(self):
        return  f"Event Payment record id : {self.id}, gateway id : {self.id_payment_gateway_reference}"