import time
import datetime

def say():
    while True:
        print("now: {0}".format(datetime.datetime.now()))
        time.sleep(10)
