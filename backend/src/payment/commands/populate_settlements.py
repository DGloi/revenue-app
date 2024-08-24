from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the Payment table from psp reports'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO payment_eventpayment
                (
                        id_payment_gateway_reference, 
                        id_transaction, 
                        id_product, 
                        id_invoice_number, 
                        amount_net, 
                        amount_discount,
                        amount_tax,
                        amount_total, 
                        amount_payment_gateway, 
                        amount_credit,
                        currency,
                        name_payment_gateway,
                        country_tax_address,
                        country_ip, 
                        date_invoice,
                        date_transaction, 
                        date_billing_period_start, 
                        date_billing_period_end,
                        name_subscription_description,
                        meta_invoice_origin, 
                        meta_data_origin, 
                        meta_tax_origin,
                        meta_payment_method, 
                        meta_report_timezone
                           )
                SELECT 
                        i.pspReference,
                        p.id_transaction,
                        p.id_product,
                        p.id_invoice_number,
                        p.amount_net,
                        p.amount_discount,
                        p.amount_tax,
                        p.amount_total,
                        mainAmount,
                        p.amount_credit,
                        COALESCE(p.currency, mainCurrency),
                        "Adyen",
                        p.country_tax_address,
                        p.country_ip,
                        p.date_invoice,
                        i.bookingDate,
                        
                FROM import_adyenpaymentaccountingreport i
                LEFT JOIN payment_eventpayment p  ON i.pspReference = p.id_payment_gateway_reference
                WHERE NOT EXISTS (
                    SELECT 1 
                    FROM payment_payment AS payment
                    WHERE payment.pspReference = source1.pspReference
                )
                );
            ''')
            connection.commit()

        self.stdout.write(self.style.SUCCESS('Payments populated successfully'))