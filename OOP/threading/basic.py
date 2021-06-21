import threading
import logging
import time
import random

def create_thread(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finish", name)

if __name__ == '__main__':

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("main  : before creating threading")

    for index in range(10):
        x = threading.Thread(
            target=create_thread, 
            args=(index,)
            )
        x.start()
        logging.info("Main  : wait for the tread to finish")
        logging.info("Main  : all done")    


#source: https://realpython.com/intro-to-python-threading/