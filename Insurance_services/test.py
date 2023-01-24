
# some_list = []
#
#
#
# a = True
# idx = 0
#
# while True:
#     b = not + a
#     a = not + a
#     idx += 1
#     print(f'{idx} -- step {b}')
#     if idx == 1000:
#         break

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

print(is_year_leap(2023))


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




print(days_in_month(2023, 6))



# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")