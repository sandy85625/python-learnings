
"""
BankAccount that inherits CIF with additional attributes like account_number (which is a random number), 
account type, balance, date_of_opening, and methods like open_Account (to open a bank account), deposit, 
withdraw, and check_balance.

Implement functions:
- open_account
- deposit
- withdraw
- check_balance

CIF takes name, address and phone as initialization.
BankAccount takes Inherited initalization of CIF and account_number, account_type, balance and date_of_opening

"""

import random
from datetime import datetime

class CIF:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class BankAccount(CIF):
    def __init__(self, name, address, phone, account_type):
        super().__init__(name, address, phone)
        self.account_number = random.randint(1000000000, 9999999999)  # 10-digit random account number
        self.account_type = account_type
        self.balance = 0
        self.date_of_opening = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def open_account(self):
        print("\nYour account has been opened successfully!")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Holder Address: {self.address}")
        print(f"Account Holder Phone: {self.phone}")
        print(f"Account Type: {self.account_type}")
        print(f"Date of Opening: {self.date_of_opening}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully! New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("\nInsufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully! New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


# Create a new BankAccount object
account = BankAccount("Devika KB", "Govt Engg Clg, Sreekrishnapuram.", "555-555-5555", "Savings")

# Open the account
print('\nOpening an account with details: "Devika KB", "Govt Engg Clg, Sreekrishnapuram.", "555-555-5555", "Savings"')
account.open_account()

# Deposit some money
print("\nDepositing 1000Rs")
account.deposit(1000)

# Withdraw some money
print("\nWithdrawing 500Rs")
account.withdraw(500)

# Check the current balance
print("\nCheck balance")
account.check_balance()
