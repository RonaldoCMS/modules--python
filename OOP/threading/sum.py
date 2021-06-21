import threading
import time
import random
import logging

def sum(num1, num2, number):
    time.sleep(random.randint(1,5))
    print("sum number:\t", number, "\t:", (num1 + num2))

if __name__ == '__main__':
    i = 0
    while i < 10:
        thread = threading.Thread(target=sum, args=(random.randint(1,5),random.randint(1,5),i))
        thread.start()
        i+=1
    print("Finish")