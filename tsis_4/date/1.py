import datetime

today = datetime.datetime.now()
subtract_days = datetime.timedelta(days=5)
result = today - subtract_days
print("Today's date:", today)
print("Subtracting 5 days, the new date is:", result)