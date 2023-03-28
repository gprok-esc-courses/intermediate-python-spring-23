

class Model:
    def __init__(self):
        self.x = 200
        self.y = 200

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

