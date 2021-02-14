from csv import reader
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]


import datetime as dt # NOTE: importing as alias

import datetime as dt
ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)
print(ibm_founded)
print(man_on_moon)

date_format = "%m/%d/%y %H:%M"

for row in potus:
    appt_start_date = row[2]
    date = dt.datetime.strptime(appt_start_date, date_format)
    row[2] = date


visitors_per_month = {}

for row in potus:
    appt_start_date = row[2]
    date = dt.datetime.strftime(appt_start_date,'%B, %Y')
    if date not in visitors_per_month:
        visitors_per_month[date] = 1
    else:
        visitors_per_month[date] +=1

# NOTE: Assign the datetime object stored at index value 2 to a variable.
# NOTE: Append the time object to the appt_times list.
appt_times = []

for row in potus:
    appt_dt = row[2]
    appt_t = appt_dt.time()
    appt_times.append(appt_t)


min_time = min(appt_times)
max_time = max(appt_times)
print(min_time)
print(max_time)


dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)
answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)
