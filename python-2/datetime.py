#!/usr/bin/python

import datetime

print datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print datetime.date.today().strftime("%Y%m%d")
print datetime.date.today().strftime("%A, %d %B, %Y")
print datetime.date.today().strftime("Today is %j day of the year %Y")