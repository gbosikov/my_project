def is_year_leap(year):
    """
    takes year as int and returns True if year is leap
    :param year:
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

print(is_year_leap(1600))


def days_in_month(year, month):
    """
    retuns days count in month
    :param year:
    :param month:
    :return:
    """
    if month in range(1, 13):
        if month == 2:
            if is_year_leap(year):
                days = 29
            else:
                days = 28
            return days
        else:
            days = 30 + (month + month // 8) % 2
            return days
    return f'month range must be 1- 12'


def day_of_year(year, month, day):
    day_of_weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_date = [1601, 1, 1, day_of_weeks[0]]
    in_month = days_in_month(year, month)
    days_in_year = 0
    day_in_m = 0
    for d in range(start_date[0], year):
        if is_year_leap(d):
            days_in_year += 366
        else:
            days_in_year += 365
    for x in range(start_date[1], month):
        day_in_m += days_in_month(year, x)
    total = days_in_year + day_in_m + day - 1
    a = total % 7
    return day_of_weeks[a]


print(day_of_year(2000, 12, 31))



some_lsr = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

user_inp = input('Enter some digit from 1 to 9: \n')

for row in range(3):
    for col in range(3):
        print(row, col)
        move = False
