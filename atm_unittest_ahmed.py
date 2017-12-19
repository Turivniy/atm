from atm import *

import unittest

class TestAtm(unittest.TestCase):

    def setUp(self):
        self.terminal = Atm()
        self.terminal.enter_pin(777)
        self.attempts = Atm()
        self.attempts = 2

    def test_rise_money(self):
        '''Test that client can put money in his account'''
        rise_money = self.terminal._rise_money(500)
        self.assertEqual(10500, rise_money)

    def test_withdraw_money_true(self):
        '''Test that client can withdraw money from his account (when money < = balance)'''
        withdraw_money_1 = self.terminal.get_money(700)
        self.assertEqual(700, withdraw_money_1)

    def test_withdraw_money_false(self):
        '''This test should be failed because client doesn't have enough money to withdraw'''
        withdraw_money_2 = self.terminal.get_money(10001)
        self.assertEqual(10001, withdraw_money_2)

    def test_correct_pin(self):
        '''Check that client enter the correct pin code'''
        self.assertTrue(self.terminal.enter_pin(777))

    def test_attempts_true(self):
        '''Test that client has only 2 attempts to input pin code'''
        self.assertEqual(self.attempts, 2)

    def test_attempts_false(self):
        '''Test should be failed because client has only 2 attempts'''
        self.assertEqual(self.attempts, 3)

    def test_check_balance(self):
        '''Test that client can check his balance'''
        self.assertTrue(self.terminal.check_balance())


if __name__ == '__main__':
    unittest.main()
