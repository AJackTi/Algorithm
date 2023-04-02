# 11/11/2017
# Author: AJackTi

# First, I will create list with many random numbers
from random import randint

def create_list():
	return [randint(1,100) for i in range(20)]

def inserttion(lst):
	for i in range(1,len(lst)):
		j = i - 1
		if lst[i] > lst[j]:
			continue
		while j >= 0 and lst[i]<lst[j]:
			key = j
			j = j - 1
		try:
			lst.insert(key,lst[i])
			key = -1
			del lst[i+1]
		except:
			pass

	print (lst)

if __name__ == "__main__":
	lst = create_list()
	print (lst)
	inserttion(lst)