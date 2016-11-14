# Josh Dickey 11/11/16
# this program creates a class that allows deposits and withdraw's to be made to accounts


class Account:
    """this identifies the name of the person, their account number, and their balance in that account"""
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """this increases the amount of money in that persons account when they receive a deposit"""
        self.balance += amount

    def withdraw(self, amount):
        """
        this reduces the amount of money in that persons account when they
        withdraw and tells them if they can withdraw that amount
        """
        if amount < self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def show_balance(self):
        """this shows the balance of a persons account"""
        return self.balance

    def __str__(self):
        """this is the string function that displays the amount of money they have in their account"""
        return self.name + " has " + str(self.balance) + " in account number " + str(self.account_number)
