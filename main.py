import telebot
from telebot import types

from constant import token
from schedule import Schedule
from different import string_timing

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()

    first_button = types.KeyboardButton("Current double-period")
    second_button = types.KeyboardButton("Today's schedule")
    third_button = types.KeyboardButton("/stop")

    markup.row(first_button, second_button)
    markup.row(third_button)

    bot.send_message(message.chat.id, "HNEU scheduler is working..", reply_markup=markup)


@bot.message_handler(commands=["stop"])
def handle_stop(message):
    hide_markup = types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, "HNEU scheduler was stopped", reply_markup=hide_markup)


@bot.message_handler(func=lambda m: m.text == "Current double-period")
def get_current_double_period(message):
    current_double_period = Schedule.get_current_double_period()

    if current_double_period is None:
        response_message = "There is no double-period now"
    else:
        response_message = "Current double-period: \n\nNumber: {}\nSubject: {}\nSubject type: {}\nPlacement: {}\n" \
                           "Lecturer: {}\nTime to end: {}".format(current_double_period[0]["number"],
                                                                  current_double_period[0]["subject"],
                                                                  current_double_period[0]["subject_type"],
                                                                  current_double_period[0]["placement"],
                                                                  current_double_period[0]["lecturer"],
                                                                  current_double_period[1])

    bot.send_message(message.chat.id, response_message)


@bot.message_handler(func=lambda m: m.text == "Today's schedule")
def get_current_schedule(message):
    current_schedule = Schedule.get_current_schedule()

    if current_schedule[0] == 0:
        response_message = "There are no double-periods today"
    else:
        response_message = "There are {} double-periods today: \n\n".format(current_schedule[0])

        for actual_double_period in current_schedule[1]:
            member = "Number: {}\nSubject: {}\nSubject type: {}\nPlacement: {}\n" \
                     "Lecturer: {}\nTiming:\n{}\n\n".format(actual_double_period["number"],
                                                            actual_double_period["subject"],
                                                            actual_double_period["subject_type"],
                                                            actual_double_period["placement"],
                                                            actual_double_period["lecturer"],
                                                            string_timing[actual_double_period["number"] - 1])
            response_message += member

    bot.send_message(message.chat.id, response_message)


if __name__ == "__main__":
    bot.polling()
