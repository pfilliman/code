import Food
from time import sleep
import Restaurant

class Pizza():
    def __init__(self):
        pass

    def price(self):
        return 6.99

    def __str__(self):
        return f"Pizza: {self.price()}"

    def prepare(self):
        print("Pizza: Make dough.")
        sleep(1)
        print("Pizza: Roll dough.")
        sleep(1)
        print("Pizza: Put on tomato sauce.")
        sleep(1)
        print("Pizza: Put on cheese.")
        sleep(1)
        print("Pizza: Put on toppings.")
        sleep(1)
        print("Pizza: Bake pizza.")
        sleep(1)
        print("Pizza: All done!")
