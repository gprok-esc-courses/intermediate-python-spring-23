
class Client:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return self.name + ", addr: " + self.address + ", phone: " + self.phone


if __name__ == '__main__':
    client = Client("John", "High str. 34", "697845654")
    print(client)

