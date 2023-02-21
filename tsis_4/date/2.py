import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday's date:", yesterday.strftime("%m/%d/%Y"))
print("Today's date:", today.strftime("%m/%d/%Y"))
print("Tomorrow's date:", tomorrow.strftime("%m/%d/%Y"))