***This is a realization of telegram-bot which helps students get double-period's schedule data***
- To start using product you need to create your own telegram-bot token and paste it into the token="" in constant.py
- The functional consists of two modules - main.py - where the logic of bot is stored and (scheduler.py || time_manager/py):
    1) scheduler.py is used to get schedule data from university webservice and paste it into the schedule.json
    2) if you want to get data once, you just run scheduler.py, but if you want to deploy it to Heroku(for example) bot has
       to get data regularly without your impact. For this purpose you need to run time_manager.py !!parallel!! with the
       main.py.


