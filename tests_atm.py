import unittest

from atm import Atm
from atm_exceptions import *


class TestAtmPinBlock(unittest.TestCase):
    """
    Testing block with a pin input
    """

    def setUp(self):
        self.term = Atm()

    def test_input_correct_pin_and_get_balance(self):

        self.term.enter_pin(777)
        bal = self.term.check_balance()
        self.assertEqual(bal, 10000)

    def test_input_wrong_pin_three_times_and_get_error_message(self):

        try:
            self.term.enter_pin(111)
            self.term.enter_pin(111)
            self.term.enter_pin(111)
        except IncorrectPin as e:
            pass
        except AttemptsOver as e:
            self.assertEqual('Attempts are over!!!', e.message)

    def test_input_wrong_pin_two_times_then_correct_and_get_balance(self):

        try:
            self.term.enter_pin(111)
            self.term.enter_pin(111)
            self.term.enter_pin(777)
            bal = self.term.check_balance()
            self.assertEqual(bal, 10000)
        except IncorrectPin as e:
            pass

    def test_input_pin_value_more_than_three_characters(self):

        try:
            self.term.enter_pin(8888)
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_input_pin_value_less_than_three_characters(self):

        try:
            self.term.enter_pin(88)
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_input_pin_value_string(self):

        try:
            self.term.enter_pin("something")
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_input_pin_value_char(self):

        try:
            self.term.enter_pin('A')
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_input_pin_value_empty(self):

        try:
            self.term.enter_pin("")
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_input_pin_value_space(self):

        try:
            self.term.enter_pin(" ")
        except Exception as e:
            self.assertEqual("Incorrect Pin!!!", e.message)

    def test_without_input_pin_check_balance(self):

        try:
            self.term.check_balance()
        except Exception as e:
            self.assertEqual("Enter pin first!!!", e.message)

    def test_without_input_pin_get_money(self):

        try:
            self.term.get_money(1000)
        except Exception as e:
            self.assertEqual("Enter pin first!!!", e.message)

    def test_without_input_pin_rise_money(self):

        try:
            self.term._rise_money(1000)
        except Exception as e:
            self.assertEqual("Enter pin first!!!", e.message)


class TestAtmMoneyBlock(unittest.TestCase):
    """
    Testing block with a cash transactions
    """

    def setUp(self):
        self.term = Atm()
        self.term.enter_pin(777)

    def test_rise_money(self):

        rise = self.term._rise_money(1000)
        self.assertEqual(rise, 11000)

    def test_get_money(self):
        get = self.term.get_money(1000)
        balance = self.term.check_balance()
        self.assertEqual(balance, 10000 - get)

    def test_rise_money_with_negative_value(self):

        try:
            self.term._rise_money(-1000)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_rise_money_with_zero_value(self):

        try:
            self.term._rise_money(0)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_rise_money_with_very_big_value(self):

        try:
            self.term._rise_money(999999999)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_rise_money_with_string_value(self):

        try:
            self.term._rise_money("Something")
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_rise_money_with_character_value(self):

        try:
            self.term._rise_money('A')
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_get_money_with_negative_value(self):

        try:
            self.term.get_money(-1000)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_get_money_with_zero_value(self):

        try:
            self.term.get_money(0)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_get_money_with_very_big_value(self):

        try:
            self.term.get_money(999999999)
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_get_money_with_string_value(self):

        try:
            self.term.get_money("Something")
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)

    def test_get_money_with_character_value(self):

        try:
            self.term.get_money('A')
        except Exception as e:
            self.assertEqual("Atm balance is no enough!!!", e.message)


if __name__ == '__main__':
    unittest.main()
