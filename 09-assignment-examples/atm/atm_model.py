import csv


class Atm:
    def __init__(self):
        self.accounts = []

    def load_data(self):
        file = open('accounts.csv')
        counter = 0

        reader = csv.reader(file, delimiter=',')

        for row in reader:
            if counter != 0:
                self.accounts.append(row)
            counter += 1

    def print_accounts(self):
        for row in self.accounts:
            print(row)

    def get_account(self, acc_no, pin):
        for row in self.accounts:
            if row[0] == acc_no and row[1] == pin:
                return row
        return None

    # save all accounts on exit
    def save(self):
        pass


if __name__ == '__main__':
    atm = Atm()
    atm.load_data()
    atm.print_accounts()

    print(atm.get_account('1001', '1234'))
    print(atm.get_account('1001', '1224'))


