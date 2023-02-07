
class Car:
    def __init__(self, plate, color):
        self.plate = plate
        self.color = color
        self.max_speed = 150

    def change_color(self, color):
        # Check if this is a valid color
        self.color = color

    def __str__(self):
        return "Car, plate: " + self.plate + ", color: " + self.color


a = Car("ABC6734", "white")
a.color = "lskdjfbsdkljfnbsdj"
b = Car("CDE6712", "black")
b.color = "yellow"

print(a)
print(b)
