"mean.py"
import sys

#sum input values
sum = 0
n = 0
for num in sys.stdin:
	sum += float(num)
	n += 1
print sum / n

