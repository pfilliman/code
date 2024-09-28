from Restaurant import *

def main():
    r = Restaurant() 
    food = r.order_food("cheeseburger") 
    if food: 
        print(food) 
     
    food = r.order_food("pasta") 
    if food: 
        print(food) 
     
    food = r.order_food("mac and cheese")  # doesn't exist, prints failure message 
    if food: 
        print(food)

    food = r.order_food("Pizza")
    if food: 
        print(food) 

    r2 = Restaurant()
    print(r2)

if __name__ == "__main__": 
    main()
