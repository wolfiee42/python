
import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y ")


target_date = datetime.datetime(2020, 1, 2, 12, 30, 0)
current_Date = datetime.datetime.now()


if target_date < current_Date:
    print("Target date has passed.")
else:
    print("Target date NOT has passed.")


# print(now)