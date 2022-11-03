# Getting more control over formatting
from datetime import datetime

now = datetime.now()


#strftime: string from time.
print(now.strftime("%a %A %d"))
#%a day of week: MOn, Tues, Wed...
#%A full name of week: Monday, Tuesday, wednesday...
#%d is day of week

print(now.strftime("%b %B %m"))
#%a day of month: Jan, Feb,...
#%A full name of month: January, February,....
#%m month of the year.

print(now.strftime("%A %B %d"))

print(now.strftime("%H : %M : %S %p"))

print(now.strftime("%y %Y"))
%p is AM or PM