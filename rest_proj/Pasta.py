import Food
from time import sleep
import Restaurant

class Pasta():
    def __init__(self):
        pass

    def price(self):
        return 8.99

    def __str__(self):
        return f"Pasta: {self.price()}"

    def prepare(self):
        print("Pasta: Boil water.")
        sleep(1)
        print("Pasta: saute onions, garlic and tomatoes for sauce.")
        sleep(1)
        print("Pasta: put noodles in water.")
        sleep(1)
        print("Pasta: season the sauce.")
        sleep(1)
        print("Pasta: plate noodles and add sauce on top.")
        sleep(1)
        print("Pasta: All done!")

        return True

