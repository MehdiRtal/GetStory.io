import datetime

now = datetime.datetime.now(datetime.timezone.utc)
time = datetime.datetime(2023, 3, 30, 11, 45, 25, tzinfo=datetime.timezone.utc)
print(time)
print(now)
print(now-time)