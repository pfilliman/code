import Food
from time import sleep
import Restaurant

class Cheeseburger():
    def __init__(self):
        pass

    def price(self):
        return 5.99

    def __str__(self):
        return f"Cheeseburger: {self.price()}"

    def prepare(self):
        print("Cheeseburger: Grill hamburger.")
        sleep(1)
        print("Cheeseburger: Flip hamburger.")
        sleep(1)
        print("Cheeseburger: Put on cheese.")
        sleep(1)
        print("Cheeseburger: Put on bun.")
        sleep(1)
        print("Cheeseburger: All done!")
