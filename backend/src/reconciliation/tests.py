from django.test import TestCase


class ReconciliationTestCase(TestCase):
    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)
