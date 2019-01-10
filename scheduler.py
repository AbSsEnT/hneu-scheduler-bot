# This is a scheduler for a specific group - 6.04.121.010.18.1
# This module was hardcoded

import json

from requests_html import HTMLSession

week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

request = HTMLSession().request("get", "http://services.hneu.edu.ua:8081/schedule/schedule?group=25524")

with open("schedule.json", "w", encoding="utf-8") as file:
    schedule = []
    work_days = len(request.html.find("body > table:nth-child(2) > tr:nth-child(1) > *")) - 1

    for day in range(1, work_days + 1):
        week_day = {}
        double_periods = []
        double_periods_quantity = len(request.html.find("body > table:nth-child(2) > *")) - 1

        # Make an exception for saturday and sunday
        for double_period in range(2, double_periods_quantity + 2):
            is_empty = False

            data = request.html.find("body > table:nth-child(2) > tr:nth-child({}) > *".format(double_period))[day]\
                .text.split('\n')

            if len(data) == 1:
                is_empty = True
                data = ["-"] * 4

            double_periods.append({
                "number": double_period - 1,
                "is_empty": is_empty,
                "subject": data[0],
                "subject_type": data[1],
                "placement": data[2],
                "lecturer": data[3]
            })

        week_day["day"] = week_days[day - 1]
        week_day["schedule"] = double_periods

        schedule.append(week_day)

    json.dump(schedule, file, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
