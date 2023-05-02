
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount: int):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Not sufficient balance")
        except TypeError:
            print("Invalid type of data")

    def get_balance(self):
        return self.balance

# 100.000 lines code


if __name__ == '__main__':
    b = BankAccount()
    b.withdraw("ABCD")
    print(b.get_balance())

