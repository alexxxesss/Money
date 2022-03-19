import unittest
from class_Money import Money


bank_account1 = Money(3000.23, "CZK")
bank_account2 = Money(150, "USD")
bank_account3 = Money(200, "EUR")
bank_account4 = Money(99.77, "CZK")


class MyTestCase(unittest.TestCase):
    def test_1_type_error(self):
        with self.assertRaises(TypeError):
            bank_account1 + bank_account2

    def test_2_add(self):
        bank_account5 = bank_account1 + bank_account4
        self.assertEqual(bank_account5.value, 3100)

    def test_c(self):
        self.assertTrue(bank_account3 > bank_account2)

