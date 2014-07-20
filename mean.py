"mean.py"
#print the mean
#changes to big_file

import sys
#it is important to import the system in order to call python functions
#sum input values
sum = 0
n = 0
for num in open('data.txt'):
	sum += float(num)
	n += 1
print sum / n
#determine mean of data.txt
