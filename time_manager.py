import os

from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    os.system("python scheduler.py")


schedule = BlockingScheduler()

schedule.add_job(job_function, 'cron', hour='8-20')

if __name__ == "__main__":
    schedule.start()
