from abc import ABC, abstractmethod
from faker import Faker
import random


class Account(ABC):
    def __init__(self, aid: int, name: str):
        self.id = aid
        self.name = name
        self.balance = 0

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount

    def get_balance(self) -> float:
        return self.balance

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return str(self.id) + " " + self.name + " " + str(self.balance)


class Checking(Account):
    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance:
            print("Invalid amount")
        else:
            self.balance -= amount


class Savings(Account):
    def withdraw(self, amount: float) -> None:
        if amount <= 0 or amount > self.balance or amount > 200:
            print("Invalid amount")
        else:
            self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def add(self, account: Account) -> None:
        if account.id in self.accounts:
            print("Account already exists")
        else:
            self.accounts[account.id] = account

    def load_accounts(self):
        for i in range(20, 100):
            t = random.randint(0, 1)
            if t == 0:
                bank.add(Checking(i, fake.first_name() + " " + fake.last_name()))
            else:
                bank.add(Savings(i, fake.first_name() + " " + fake.last_name()))

    def print_accounts(self):
        for acc in bank.accounts:
            print(bank.accounts[acc])

    def get_account(self, aid: int) -> Account:
        if aid in self.accounts:
            return self.accounts[aid]
        else:
            return None


# From this point we are in another part of the program, some other programmer is doing that
if __name__ == '__main__':
    fake = Faker()
    bank = Bank()
    bank.load_accounts()
    bank.print_accounts()

    while True:
        aid = int(input("ID (0 to close): "))
        if aid == 0:
            break
        acc = bank.get_account(aid)
        if acc is None:
            print("Account does not exist")
            continue
        print("Welcome " + acc.get_name())
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("0. EXIT")
            choice = int(input("Choose: "))
            if choice == 1:
                am = float(input("Amount: "))
                acc.deposit(am)
            elif choice == 2:
                am = float(input("Amount: "))
                acc.withdraw(am)
            elif choice == 3:
                print("Balance:", acc.get_balance())
            elif choice == 0:
                break
            else:
                print("Wrong choice")




