from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the Payment table from psp reports'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO payment_eventpayment
                (id_payment_gateway_reference, id_transaction, id_product, id_invoice_number, amount_net, 
                        amount_discount, amount_tax, amount_total, amount_payment_gateway, amount_credit,
                        currency, name_payment_gateway, country_tax_address, country_ip, date_invoice, date_transaction, 
                        date_billing_period_start, date_billing_period_end, name_subscription_description, meta_invoice_origin, 
                        meta_data_origin, meta_tax_origin, meta_payment_method, meta_report_timezone)
                SELECT source1.pspReference, source1.field1, source1.field2, ...
                FROM import_source1 AS source1
                WHERE NOT EXISTS (
                    SELECT 1 
                    FROM payment_payment AS payment
                    WHERE payment.pspReference = source1.pspReference
                )

                );
            ''')
            connection.commit()

        self.stdout.write(self.style.SUCCESS('Payments populated successfully'))