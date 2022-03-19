import datetime
import random
import re


def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs(d1 - d2)


def i_have_no_vinaigrette():
    date1, date2 = input("Enter two dates in format YYYY-MM-DD and date1 smaller than date2: ").split()
    if re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', date1) and re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', date2) and date1 < date2:
        time_between_dates = days_between(date1, date2)
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = datetime.datetime.strptime(date1, "%Y-%m-%d") + datetime.timedelta(days=random_number_of_days)
        print(random_date.date())

    else:
        print("Invalid input")


i_have_no_vinaigrette()
