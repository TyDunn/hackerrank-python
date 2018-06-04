import calendar

month, day, year = list(map(int, input().split()))

weekday = calendar.weekday(year, month, day)

print((calendar.day_name[weekday]).upper())