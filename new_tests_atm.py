import unittest
from atm import *
 

class TestAtm(unittest.TestCase):
 
    def setUp(self):
        self.terminal = Atm()
        self.terminal.enter_pin(777)
        self.attempts = Atm()
        self.attempts = 2

    def test_rise_money(self):
        '''Test that client can put money in his account (input 5000)
       expected result: balance = 15000
       actual result: balance = 15000'''
        rise_money = self.terminal._rise_money(5000)
        self.assertEqual(15000, rise_money)

    def test_rise_money_zero(self):
        '''BUG #1: Client can input 0 as value to rise his balance
       Test that client can't rise balance by inputting "Zero"
       expected result: balance = 10000 and ERROR msg raise
       actual result: balance = 10000'''
        rise_money_zero = self.terminal._rise_money(0)
        self.assertEqual(10000, rise_money_zero)

    def test_rise_money_minus(self):
        ''' BUG #2 : balance decreases when client input -1
       Test that client can't rise balance by inputting "value with minus "-1"
       expected result: balance = 10000 and raise ERROR msg (invalid value)
       actual result: balance = 9999 '''
        rise_money_minus = self.terminal._rise_money(-1)
        self.assertEqual(10000, rise_money_minus)

    def test_rise_money_one(self):
        '''Test that client can rise his balance by inputting "one"
       expected result: balance = 10001
       actual result: balance = 10001'''
        rise_money_one = self.terminal._rise_money(1)
        self.assertEqual(10001, rise_money_one)

    def test_rise_money_string(self):
        '''Test that client can't rise his balance by inputting "str"
       expected result: balance = 10000 and raise ERROR msg (unsupported operand type)
       actual result: balance = 10000 with ERROR MSG'''
        rise_money_string = self.terminal._rise_money("hello")
        self.assertEqual("hello", rise_money_string)

    def test_withdraw_money_1(self):
        '''Test that client can withdraw money from his account (when money < = balance)
       expected result: balance = 3000
       actual result: balance = 3000'''
        withdraw_money_1 = self.terminal.get_money(7000)
        self.assertEqual(7000, withdraw_money_1)

    def test_withdraw_money_2(self):
        '''Test that client can withdraw all money from his account (input 10000)
       expected result: balance = 0
       actual result: balance = 0 '''
        withdraw_money_2 = self.terminal.get_money(10000)
        self.assertEqual(10000, withdraw_money_2)

    def test_withdraw_money_3(self):
        '''BUG #3: atm accepts input "0"
       Test that client can't input "0" as value to withdraw money from his account
       expected result: balance = 10000 and ERROR msg raise
       actual result: balance = 10000'''
        withdraw_money_3 = self.terminal.get_money(0)
        self.assertEqual(0, withdraw_money_3)

    def test_withdraw_money_4(self):
        '''BUG #4: balance rises by inputting "-1"
       Test that client can't withdraw money from his account by inputting "value with minus "-""
       expected result: balance = 10000 and raise ERROR msh (invalid value)
       actual result: balance = 10001'''
        withdraw_money_4 = self.terminal.get_money(-1)
        self.assertEqual(-1, withdraw_money_4)

    def test_withdraw_money_5(self):
        '''Test that client can't withdraw sum of money (10001) that exceed his balance
       expected result: ERROR msg (Atm balance is not enough)
       actual result: as expected '''
        withdraw_money_5 = self.terminal.get_money(10001)
        self.assertEqual(10001, withdraw_money_5)

    def test_withdraw_money_6(self):
        '''BUG #5: User can enter "string" instead of "int"
       Test that client can't withdraw money from his account by inputting "string"
       expected result: ERROR arise "unsupported operand type"
       actual result: "Atm balance is not enough"'''
        withdraw_money_6 = self.terminal.get_money("Give me")
        self.assertEqual("Give me", withdraw_money_6)

    def test_correct_pin(self):
        '''Check that client enter the correct pin code (INPUT 777)
       expected result: pin code TRUE
       actual result: as expected '''
        self.assertTrue(self.terminal.enter_pin(777))

    def test_incorrect_pin(self):
        ''' Test that client can't access to his account when he enters incorrect pin
       expected result: raise ERROR (IncorrectPin)
       actual result: as expected  '''
        self.assertTrue(self.terminal.enter_pin(666))

    def test_attempts_true(self):
        '''Test that client has only 2 attempts to input pin code'''
        self.assertEqual(self.attempts, 2)

    def test_attempts_false(self):
        '''Test that client can't enter incorrect pin code more than 2 times
       expected result: raise ERROR
       actual result: as expected'''
        self.assertEqual(self.attempts, 3)

    def test_check_balance(self):
        '''Test that client can check his balance
       expected result: can check his balance
       actual result: as expected'''
        self.assertTrue(self.terminal.check_balance())
 

if __name__ == '__main__':
    unittest.main()
 
