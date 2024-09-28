from asyncio import QueueEmpty
from queue import Empty
from random import randint
from threading import Semaphore, Thread, Lock
from logging import basicConfig, debug, DEBUG
from time import sleep
from Customer import *
from Teller import *

def bankprint(lock, msg):
    lock = Lock()
    print(msg)


def wait_outside_bank(customer, guard, teller_line, printlock):
    bankprint(printlock, f"(C) 'Customer {customer.name}' waiting outside bank")
    
    try:
        semaphore = guard
    except:
        print("Exception occurred getting semaphore.")

    print(f"<G> Security guard letting 'Customer {customer.name}' into the bank")
    print(f"(C) 'Customer {customer.name}' getting into line")
    teller_line.put(customer)


def teller_job(teller, guard, teller_line, printlock):
    teller_timeout = 10         # longest time that a teller will wait for new customers 

    print(f"[T] 'Teller {teller.name}' starting work")

    while 1 == 1:
        try:
            cust = teller_line.get(timeout=teller_timeout)
            print(f"[T] 'Teller {teller.name}' is now helping Customer {cust.name}'")
            sleep(randint(1, 4))
            print(f"[T] 'Teller {teller.name}' is done helping 'Customer {cust.name}'")
            print(f"<G> Security guard is letting 'Customer {cust.name}' out of the bank")

            guard.release()
        
        except Empty:
            print(f"[T] Nobody is in line, 'Teller {teller.name}' is going on break")
            break
        except QueueEmpty:
            print(f"[T] Nobody is in line, 'Teller {teller.name}' is going on break")
            break
        

