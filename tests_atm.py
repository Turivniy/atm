import unittest

from atm import Atm
from atm_exceptions import *


class TestAtm(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_atm_gives_money(self):
        money = self.atm.get_money(1000)
        self.assertEqual(1000, money)

    def test_atm_rise_money(self):
        rise = self.atm._rise_money(1000)
        self.assertEqual(11000, rise)

    def test_atm_check_balance(self):
        check = self.atm.check_balance()
        self.assertEqual(10000, check)


class TestAtmExceptions(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_exception_atm_balance(self):
        try:
            self.atm.get_money(1000000)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_exception_incorrect_pin(self):
        try:
            self.atm.enter_pin(111)
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_exception_enter_pin_first(self):
        try:
            self.atm2 = Atm()
            self.atm2.check_balance()
        except Exception as e:
            self.assertEqual("Enter pin first!!!", e.message)

    def test_exception_attempts_over(self):
        try:
            self.atm2 = Atm()
            self.atm2.__attempts = 0
        except Exception as e:
            self.assertEqual("Attempts are over!!!", e.message)


if __name__ == '__main__':
    unittest.main()
