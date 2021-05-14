'''
14. Write a Python program to calculate number of days between two dates.

'''

import datetime

date1 = datetime.datetime(1993,7,15)
date2 = datetime.datetime.now()

years = date2-date1

print(years.days)