__author__ = 'Prudhvi'

import datetime

print(datetime.date.today())
ti = datetime.time()
sti = str(ti.strftime("%Y%m%d%H%M%S"))
print(sti)

now = datetime.datetime.now()
print(str(now))
print(str(now.year) +
      str(now.month) +
      str(now.day) +
      str(now.hour) +
      str(now.minute) +
      str(now.second) +
      str(now.microsecond))

print(now.strftime('%Y%m%d%H%M%S'))
