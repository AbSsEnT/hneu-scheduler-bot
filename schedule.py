import json
from datetime import datetime


class Schedule:
    timing = [[(8, 30), (10, 5)], [(10, 15), (11, 50)], [(12, 10), (13, 45)], [(13, 55), (15, 30)],
              [(15, 50), (17, 25)], [(17, 35), (19, 10)]]

    @classmethod
    def get_current_double_period(cls):
        with open("schedule.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            current_weekday = datetime.now().weekday()

            if current_weekday >= len(data):
                return None

            data = data[current_weekday]["schedule"]
            current_time = datetime.now()
            double_period_number, time_to_end = None, None

            for number, period in enumerate(cls.timing):
                begin = datetime.now().replace(hour=period[0][0], minute=period[0][1], second=0)
                end = datetime.now().replace(hour=period[1][0], minute=period[1][1], second=0)

                if begin <= current_time <= end:
                    double_period_number = number
                    time_to_end = end - current_time

            if double_period_number is not None and double_period_number < len(data):
                data = data[double_period_number]

                if data["is_empty"] is False:
                    return data, time_to_end

            return None

    @classmethod
    def get_current_schedule(cls):
        with open("schedule.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            current_weekday = datetime.now().weekday()

            if current_weekday >= len(data):
                return None

            data = data[current_weekday]["schedule"]
            actual_double_periods = []
            actual_double_periods_quantity = 0

            for double_period in data:
                if double_period["is_empty"] is False:
                    actual_double_periods_quantity += 1
                    actual_double_periods.append(double_period)

            return actual_double_periods_quantity, actual_double_periods

