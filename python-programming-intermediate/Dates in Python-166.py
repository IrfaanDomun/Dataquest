## 1. The time module ##

import time 
current_time = time.time() 

## 2. Converting timestamps ##

import time

current_time = time.time()

current_struct_time = time.gmtime(current_time)

current_hour = current_struct_time.tm_hour

print(current_hour)

## 3. UTC ##

import datetime

current_datetime = datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

today = datetime.datetime.now()

diff = datetime.timedelta(days=1)

yesterday = today - diff

tomorrow = today + diff

## 5. Formatting dates ##

import datetime
mystery_date_formatted_string = "{0:%I}:{0:%M}{0:%p} on {0:%A} {0:%B} {0:%d}, {0:%Y}".format(mystery_date)

## 6. Parsing dates ##

import datetime

mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print( mystery_date)


## 8. Reformatting our data ##

import datetime

for i in posts:
    t = float(i[2])
    i[2] = datetime.datetime.fromtimestamp(t)
    

## 9. Counting posts in March ##

march_count = 0

for i in posts:
    if i[2].month == 3:
        march_count +=1

## 10. Counting posts in any month ##

def count(n):
    march_count = 0

    for row in posts:
        if row[2].month == n:
            march_count += 1
    return march_count
    
feb_count = count(2)
aug_count = count(8)
    