import schedule
import time
import abc
import test

def job():
    test.func()
    

schedule.every(1).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(5)
    

