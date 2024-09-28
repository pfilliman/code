from Food import *

class Restaurant(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print("Creating a new Restaurant")
            cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
            cls._instance._orders = 0
            cls._instance._total_sales = 0
        else:
            print("Using existing instance")
        
        return cls._instance


    def __str__(self):
        return f"This restaurant had {__class__._instance._orders} orders today for a total of {__class__._instance._total_sales} in sales."


    def order_food(self, food_type):
        food, price = Food.order_food(food_type)
        if price:
            __class__._instance._orders += 1
            __class__._instance._total_sales += price

        return food
        