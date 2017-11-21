# 11/11/2017
# Author: AJackTi

# First, I will create list with many random numbers
from random import randint

list = []

for i in range(100):
	list.append(randint(0,100))

print list
	
for i in range(1,len(list)):
	j = i - 1
	if list[i] > list[j]:
		continue
	while j >= 0 and list[i]<list[j]:
		key = j
		j = j - 1
	try:
		list.insert(key,list[i])
		key = -1
		del list[i+1]
	except:
		pass

print list