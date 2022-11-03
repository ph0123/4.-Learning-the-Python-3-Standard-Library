# Statistics Module
import statistics
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15,50]

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))
print(sorted(agesData))

print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))


#Output
'''
11.777777777777779
10
11
[10, 10, 10, 11, 11, 12, 13, 14, 15]
3.4444444444444446
1.855921454276674
1.855921454276674
'''