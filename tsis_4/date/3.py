import datetime

now = datetime.datetime.now()
now_without_microseconds = now.replace(microsecond=0)
print("Date/time with microseconds:", now)
print("Date/time without microseconds:", now_without_microseconds)