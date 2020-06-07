class PiggySave:

    def __init__(self):
        self.money = 0

    def add(self, amount):
        self.money += amount

    def open(self):
        total = self.money
        self.money = 0
        return total



my_Save = PiggySave()

your_Save = PiggySave()

my_Save.add(500)

my_Save.add(500)

print(my_Save.open())
print(your_Save.open())
print(my_Save.open())
