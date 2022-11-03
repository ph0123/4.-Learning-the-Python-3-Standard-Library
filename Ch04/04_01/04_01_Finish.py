# Datetime Module Part I
from datetime import datetime

now = datetime.now()

print(now.date())

print(now.year)

print(now.month)

print(now.hour)

print(now.minute)

print(now.second)

print(now.time())

#datetime can used for many purposes
#remember about "from datetime import datetime"

#output: It will be changed when you run your program.
'''
2022-11-03
2022
11
13
41
42
13:41:42.601485
'''