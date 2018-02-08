# 01.01.1900 - Monday
# 07.01.1900 - Sunday
from datetime import datetime


def is_leap(year):
    return (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def get_days_in_month(input_date):
    # month is 1..12
    month = input_date.month
    if month in [9, 4, 6, 11]:
        return 30
    if month == 2:
        if is_leap(input_date.year):
            return 29
        else:
            return 28
    return 31


def get_day_of_week_lib(input_date):
    return input_date.weekday()


def solve(start_date, end_date):
    # Question is how many Sundays
    # fell on the first of the month during the period
    # go through every month
    # calculate which day of week it was
    # if sunday, +1
    res = 0
    for year in range(start_date.year, end_date.year + 1):
        for month in range(1, 13):
            dow = get_day_of_week_lib(datetime(year, month, 1))
            if dow == 6:
                res += 1
    return res


if __name__ == "__main__":
    start = datetime(1901, 1, 1)
    end = datetime(2000, 12, 31)
    print(solve(start, end))
