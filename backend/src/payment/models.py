from django.db import models


# Create your models here.
class EventPayment(models.Model):
    id = (models.AutoField(primary_key=True),)
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
        return f"Event Payment record id : {self.id}, gateway id : {self.id_payment_gateway_reference}"


class EventRefund(models.Model):
    id = (models.AutoField(primary_key=True),)
    id_payment_gateway_reference = models.CharField(max_length=255)
    id_refunded_transaction = models.CharField(max_length=255)
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
    date_refund = models.DateTimeField()
    date_billing_period_start = models.DateTimeField()
    date_billing_period_end = models.DateTimeField()
    name_subscription_description = models.CharField(max_length=255)
    meta_invoice_origin = models.CharField(max_length=255)
    meta_data_origin = models.CharField(max_length=255)
    meta_tax_origin = models.CharField(max_length=255)
    meta_payment_method = models.CharField(max_length=255)
    meta_report_timezone = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Event Refund record id : {self.id}, gateway id : {self.id_payment_gateway_reference}"
class EventSettlement(models.Model):
    id_payment_lifecycle = models.CharField(max_length=255, unique=True, help_text="Unique fingerprint to identify a transaction at a particular stage of the payment lifecycle")
    id_payment_gateway_reference = models.CharField(max_length=255, help_text="Unique identifier issued by the payment gateway to identify the transaction")
    id_modification_reference = models.CharField(max_length=255, help_text="Identifier for the modification reference")
    id_settlement_batch = models.CharField(max_length=255, help_text="PSP identifier for the settlement batch")
    country = models.CharField(max_length=2, help_text="Country code where the card was issued")
    type_payment = models.CharField(max_length=50, help_text="The payment method used for the transaction. For example: visa, mc, amex")
    date_settlement = models.DateTimeField(help_text="Timestamp indicating when the payment was marked as settled by the PSP")
    type = models.CharField(max_length=50, help_text="The accounting record type")
    currency_gross = models.CharField(max_length=3, help_text="The three-character ISO currency code for the user-settlement currency")
    amount_gross = models.FloatField(help_text="Amount as specified by sender, before processing fees and eventual currency change")
    currency_net = models.CharField(max_length=3, help_text="The three-character ISO currency code for the psp-settlement currency")
    amount_net = models.FloatField(help_text="Amount after fees and eventual currency change")
    name_payment_gateway = models.CharField(max_length=255, help_text="Name of the payment gateway")
    meta_report_timezone = models.CharField(max_length=255, help_text="The timezone used by the PSP for reporting")

    def __str__(self):
        return self.id_payment_lifecycle


    def __str__(self):
        return f"Event Refund record id : {self.id}, gateway id : {self.id_payment_gateway_reference}"
