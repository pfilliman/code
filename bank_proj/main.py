from threading import Semaphore, Thread, Lock 
from queue import Queue, Empty 
from random import randint 
from time import sleep
from bank_utils import *

def main():
    max_customers_in_bank = 10  # maximum number of customers that can be in the bank at one time 
    max_customers = 30         # number of customers that will go to the bank today 
    max_tellers = 3             # number of tellers working today 
    
    printlock = Lock()
    teller_line = Queue(maxsize = max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)

    bankprint(printlock, "<G> Security guard starting their shift") 
    bankprint(printlock, "*B* Bank open")

    # Customers
    customers = []
    for i in range(0, max_customers):
        customer = Customer(i)
        customers.append(customer)

    customer_jobs = [Thread(
            name=f"Customer {i}", 
            target=wait_outside_bank, 
            args=(customers[i], guard, teller_line, printlock)) 
            for i in range(max_customers)]

    for j in customer_jobs:
        j.start()


    # Tellers
    sleep(5)
    bankprint(printlock, "*B* Tellers starting work")

    tellers = []
    for i in range(0, max_tellers):
        teller = Teller(i)
        tellers.append(teller)

    teller_jobs = [Thread(
            name=f"Teller {i}", 
            target=teller_job, 
            args=(tellers[i], guard, teller_line, printlock)) 
            for i in range(max_tellers)]

    for j in teller_jobs:
        j.start()

    for j in teller_jobs:
        j.join()

    print(f"*B* Bank closed ")

if __name__ == "__main__":
    main()
