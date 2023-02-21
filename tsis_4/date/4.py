import datetime

date1 = datetime.datetime(2022, 2, 1, 12, 0, 0)
date2 = datetime.datetime(2022, 2, 5, 14, 30, 0)

difference = date2 - date1
difference_in_seconds = difference.total_seconds()

print("The difference between the two dates is", difference_in_seconds, "seconds.")
