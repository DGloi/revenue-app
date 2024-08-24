# Generated by Django 5.0.6 on 2024-08-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0002_eventrefund"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventSettlements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_payment_lifecycle",
                    models.CharField(
                        help_text="Unique fingerprint to identify a transaction at a particular stage of the payment lifecycle",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "id_payment_gateway_reference",
                    models.CharField(
                        help_text="Unique identifier issued by the payment gateway to identify the transaction",
                        max_length=255,
                    ),
                ),
                (
                    "id_modification_reference",
                    models.CharField(
                        help_text="Identifier for the modification reference",
                        max_length=255,
                    ),
                ),
                (
                    "id_settlement_batch",
                    models.CharField(
                        help_text="PSP identifier for the settlement batch",
                        max_length=255,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        help_text="Country code where the card was issued", max_length=2
                    ),
                ),
                (
                    "type_payment",
                    models.CharField(
                        help_text="The payment method used for the transaction. For example: visa, mc, amex",
                        max_length=50,
                    ),
                ),
                (
                    "date_settlement",
                    models.DateTimeField(
                        help_text="Timestamp indicating when the payment was marked as settled by the PSP"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        help_text="The accounting record type", max_length=50
                    ),
                ),
                (
                    "currency_gross",
                    models.CharField(
                        help_text="The three-character ISO currency code for the user-settlement currency",
                        max_length=3,
                    ),
                ),
                (
                    "amount_gross",
                    models.FloatField(
                        help_text="Amount as specified by sender, before processing fees and eventual currency change"
                    ),
                ),
                (
                    "currency_net",
                    models.CharField(
                        help_text="The three-character ISO currency code for the psp-settlement currency",
                        max_length=3,
                    ),
                ),
                (
                    "amount_net",
                    models.FloatField(
                        help_text="Amount after fees and eventual currency change"
                    ),
                ),
                (
                    "name_payment_gateway",
                    models.CharField(
                        help_text="Name of the payment gateway", max_length=255
                    ),
                ),
                (
                    "meta_report_timezone",
                    models.CharField(
                        help_text="The timezone used by the PSP for reporting",
                        max_length=255,
                    ),
                ),
            ],
        ),
    ]
