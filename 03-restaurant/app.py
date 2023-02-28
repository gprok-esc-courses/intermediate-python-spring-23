from Restaurant import Restaurant


restaurant = Restaurant()
restaurant.add_client("aaa", "ccc", "1111")
restaurant.add_client("bbb", "ddd", "2222")
restaurant.add_item("a", "A", 12.2)
restaurant.add_item("b", "B", 23)
restaurant.add_item("c", "K", 9.4)

while True:
    print("RESTAURANT MENU")
    print("(1) Add order")
    print("(2) Add customer")
    print("(3) Revenue by item")
    print("(4) Payment by customer")
    print("(5) Display catalog")
    print("(6) Add item")
    print("(0) EXIT")

    choice = int(input("Select: "))

    if choice == 1:
        phone = input("Phone: ")
        restaurant.add_order(phone)
    elif choice == 2:
        name = input("Name: ")
        address = input("Address: ")
        phone = input("Phone: ")
        restaurant.add_client(name, address, phone)
    elif choice == 3:
        name = input("Item name: ")
        print(restaurant.item_revenue(name))
    elif choice == 4:
        phone = input("Phone: ")
        print(restaurant.customer_payments(phone))
    elif choice == 5:
        restaurant.display_catalog()
    elif choice == 6:
        name = input("Name: ")
        item_type = input("Type: ")
        price = float(input("Price: "))
        restaurant.add_item(name, item_type, price)
    elif choice == 0:
        print("Bye!")
        break
