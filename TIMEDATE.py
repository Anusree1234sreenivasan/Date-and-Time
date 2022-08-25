import datetime
print("Current date and time:datetime.datetime.now")
print("Current year:", datetime.date.today().strfttime("%Y"))
print("Month of the year:",datetime.date.today().strfttime("%B"))
print("Week number of the year:",datetime.date.today().strftime("%W"))
print("Weekday of the week:",datetime.date.today().strftime("%w"))
print("")