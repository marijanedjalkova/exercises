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


def get_day_of_week(input_date, prev_dow):
    # given a previous 1st, calculate how many days
    # were in the previous month
    # divide by 7, get remainder and add to the previous number
    if input_date.month > 1:
        year_of_prev_month = input_date.year
        prev_month = input_date.month - 1
    else:
        year_of_prev_month = input_date.year - 1
        prev_month = 12
    days = get_days_in_month(datetime(year_of_prev_month, prev_month, 1))
    remainder_of_full_weeks = days % 7
    return (remainder_of_full_weeks + prev_dow) % 7


def solve(start_date, end_date):
    # Question is how many Sundays
    # fell on the first of the month during the period
    # go through every month
    # calculate which day of week it was
    # if sunday, +1
    res = 0
    prev_dow = 0 # jan 1 1900
    for month in range(2, 13):
        prev_dow = get_day_of_week(datetime(1900, month, 1), prev_dow)
    # have calculated which dow was 01.12.1900
    for year in range(start_date.year, end_date.year + 1):
        for month in range(1, 13):
            dow = get_day_of_week(datetime(year, month, 1), prev_dow)
            if dow == 6:
                res += 1
            prev_dow = dow
    return res


if __name__ == "__main__":
    start = datetime(1901, 1, 1)
    end = datetime(2000, 12, 31)
    print(solve(start, end))
