import datetime
def findDay(day, month, year):
     date = datetime.datetime(year, month, day)
     weekday = date.weekday()
     weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
     return weekdays[weekday]
day = 31
month = 8
year = 2019
result = findDay(day, month, year)
print(result)
