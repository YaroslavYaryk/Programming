import datetime
import schedule
import time

def do_job():
    print("doing job")

schedule.every(5).seconds.do(do_job)

while True:
    schedule.run_pending()
    time.sleep(1)
