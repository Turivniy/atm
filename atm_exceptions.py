"""
ATM Exceptions
"""


class AttemptsOver(Exception):
    message = "Attempts are over!!!"


class AtmBalance(Exception):
    message = "Atm balance is no enough!!!"


class EnterPin(Exception):
    message = "Enter pin first!!!"


class IncorrectPin(Exception):
    message = "Incorrect Pin!!!"
