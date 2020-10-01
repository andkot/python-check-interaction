from datetime import datetime, date, time


# class Shift:
#     time_from: time
#     time_to: time
#     date_from: date
#     date_to: date
#     week_days: list

# A = {0, 2, 4, 6, 8}
# B = {1, 2, 3, 4, 5}
#
# print(A & B)


def is_intn_dates(interval_1: tuple, interval_2: tuple):
    t1start, t1end = interval_1[0], interval_1[1]
    t2start, t2end = interval_2[0], interval_2[1]
    return (t1start <= t2start <= t1end) or (t2start <= t1start <= t2end)


def is_intn_days(week_days_1: list, week_days_2:list):
    res = (set(week_days_1) & set(week_days_2))
    if not res:
        return False
    else:
        return True

def is_intn_times(time_1, time_2):
    t1start, t1end = time_1[0], time_1[1]
    t2start, t2end = time_2[0], time_2[1]
    return (t1start <= t2start <= t1end) or (t2start <= t1start <= t2end)



d1 = date(2000, 1, 10)
d2 = date(2000, 1, 11)
d3 = date(2000, 1, 12)
d4 = date(2000, 1, 13)

week_days_1 = [1, 2, 3]
week_days_2 = [2, 5, 6]

print(is_intn_dates((d1, d2), (d3, d4)))
print(is_intn_days(week_days_1,week_days_2))
