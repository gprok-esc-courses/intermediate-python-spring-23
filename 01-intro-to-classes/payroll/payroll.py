from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @abstractmethod
    def get_payment(self):
        pass


class Clerk(Employee):
    def __init__(self, name, phone, salary):
        super().__init__(name, phone)
        self.salary = salary

    def get_payment(self):
        return self.salary


class Manager(Clerk):
    def __init__(self, name, phone, salary, bonus):
        super().__init__(name, phone, salary)
        self.bonus = bonus

    def get_payment(self):
        return self.salary + self.bonus


class ContractWorker(Employee):
    def __init__(self, name, phone, wage, hours):
        super().__init__(name, phone)
        self.wage = wage
        self.hours = hours

    def get_payment(self):
        return self.wage * self.hours


personel = [
    Clerk("John Doe", "888888", 1200),
    Manager("Peter Doe", "777777", 5000, 800),
    ContractWorker("Mary Doe", "333333", 20, 78)
]

for p in personel:
    print(p.name, p.get_payment())


