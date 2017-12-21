
import unittest

from atm import Atm
from atm_exceptions import *


def setUpModule():
    print "Setup before all"

def tearDownModule():
    print "Tear Down after all"


class TestAtm(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)



    def test_enter_true_pin_and_check_balance(self):
        '''Enter the correct pin and check the balance'''
        balance = self.atm.check_balance()
        self.assertEqual(10000, balance)

    def test_gives_4000_money(self):
        '''Give money in the amount of 4000'''
        money = self.atm.get_money(4000)
        self.assertEqual(4000, money)

    def test_gives_10000_money(self):
        '''Give money in the amount of 10000'''
        money = self.atm.get_money(10000)
        self.assertEqual(10000, money)

    def test_gives_9999_money(self):
        '''Give money in the amount of 9999'''
        money = self.atm.get_money(9999)
        self.assertEqual(9999, money)

    def test_gives_0_money(self):
        '''Give money in the amount of 0'''
        money = self.atm.get_money(0)
        self.assertEqual(0, money)

    @unittest.skip("Bug #0001")
    def test_gives_min_1_money(self):
        '''A negative amount is given'''
        money = self.atm.get_money(-1)
        self.assertEqual(0, money)

    def test_rise_1000000_money(self):
        '''Add the amount of 1000000'''
        rise_money = self.atm._rise_money(1000000)
        self.assertEqual(1010000, rise_money)

    def test_rise_0_money(self):
        '''Add the amount of 0'''
        rise_money = self.atm._rise_money(0)
        self.assertEqual(10000, rise_money)

    @unittest.skip("Bug #0002")
    def test_rise_min_1_money(self):
        '''A negative amount is added'''
        rise_money = self.atm._rise_money(-1)
        self.assertEqual(10000, rise_money)




class TestAtmExceptions(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)
        self.atm2 = Atm()

    def test_gives_10001_money(self):
        '''Trying to give the amount more available'''
        try:
            self.atm.get_money(10001)
        except Exception as e:
            self.assertEqual('Atm balance is no enough!!!', e.message)

    def test_incorrect_pin(self):
        '''Testing an incorrect pin'''
        try:
            self.atm2.enter_pin(77)
        except Exception as e:
            self.assertEqual('Incorrect Pin!!!', e.message)



if __name__ == '__main__':
    unittest.main()


