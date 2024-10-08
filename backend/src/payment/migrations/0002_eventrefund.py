# Generated by Django 5.0.6 on 2024-07-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventRefund",
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
                ("id_payment_gateway_reference", models.CharField(max_length=255)),
                ("id_refunded_transaction", models.CharField(max_length=255)),
                ("id_product", models.CharField(max_length=255)),
                ("id_invoice_number", models.CharField(max_length=255)),
                ("amount_net", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "amount_discount",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("amount_tax", models.DecimalField(decimal_places=3, max_digits=10)),
                ("amount_total", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "amount_payment_gateway",
                    models.DecimalField(decimal_places=3, max_digits=10),
                ),
                ("amount_credit", models.DecimalField(decimal_places=3, max_digits=10)),
                ("currency", models.CharField(max_length=3)),
                ("name_payment_gateway", models.CharField(max_length=255)),
                ("country_tax_address", models.CharField(max_length=2)),
                ("country_ip", models.CharField(max_length=2)),
                ("date_invoice", models.DateTimeField()),
                ("date_refund", models.DateTimeField()),
                ("date_billing_period_start", models.DateTimeField()),
                ("date_billing_period_end", models.DateTimeField()),
                ("name_subscription_description", models.CharField(max_length=255)),
                ("meta_invoice_origin", models.CharField(max_length=255)),
                ("meta_data_origin", models.CharField(max_length=255)),
                ("meta_tax_origin", models.CharField(max_length=255)),
                ("meta_payment_method", models.CharField(max_length=255)),
                ("meta_report_timezone", models.CharField(max_length=255)),
            ],
        ),
    ]
