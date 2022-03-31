import datetime
import random
import re


def days_between(start_date, end_date):
    """
    The function receives two dates in string format, converts them to datetime format
    and returns a datetime object that represents the difference between start_date and end_date (in days)
    :param start_date: date in string format.
    :param end_date: date in string format.
    :return: the difference between start_date and end_date.
    """
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    return abs(start_date - end_date)


def i_have_no_vinaigrette(start_date, end_date):
    time_between_dates = days_between(start_date, end_date)
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=random_number_of_days)
    print(random_date.date())

    if random_date.weekday() == 0:
        print("I have no vinaigrette!")


if __name__ == "__main__":
    i_have_no_vinaigrette("1997-10-10", "2000-10-10")
