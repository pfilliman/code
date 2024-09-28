from Cheeseburger import *
from Pasta import *
from Pizza import *

class Food():
    def __init__(self):
        print(f"Food.__init__")

    def price(self):
        return 0

    def prepare(self):
        return 0

    @staticmethod
    def order_food(food_type):
        food_type = food_type.strip()
        try:
            type(food_type) == str
        except TypeError:
            print("TypeError occurred. Please check value of food type.")

        if food_type.lower() == "cheeseburger":
            food = Cheeseburger()
            food.prepare()
            price = food.price()
            return food, price

        if food_type.lower() == "pasta": 
            food = Pasta()
            food.prepare()
            price = food.price()
            return food, price

        if food_type.lower() == "pizza": 
            food = Pizza()
            food.prepare()
            price = food.price()
            return food, price

        if food_type.lower() not in ["cheeseburger", "pasta", "pizza"]:
            print(f"Sorry, the restaurant does not make '{food_type}'.")
            
            return False, False
