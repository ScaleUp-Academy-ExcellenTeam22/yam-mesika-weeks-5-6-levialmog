import datetime
import random
import re


def days_between(start_date, end_date):
    d1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    return abs(d1 - d2)


def i_have_no_vinaigrette(start_date, end_date):
    time_between_dates = days_between(start_date, end_date)
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=random_number_of_days)
    print(random_date.date())

    if random_date.weekday() == 0:
        print("I have no vinaigrette!")


if __name__ == "__main__":
    i_have_no_vinaigrette("1997-10-10", "2000-10-10")
