# AJack Ti
# 4/12/2017

from random import randint
import math

def createlist():
	lst = []

	for i in range(10):
		lst.append(randint(0,20))
	return lst

def radixsort(lst):
	j = 0
	sub_arr = []
	digits = int(math.log10(max(lst)))+1 
	count = 1
	while True:
		for i in lst:
			if i%(10**count) == j:
				sub_arr.append(i)
				del lst[ lst.index(i) ]
				j -= 1
		j += 1
		if not lst:
			j = 0
			count += 1
			lst = sub_arr
			sub_arr = []
			if count > digits:
				return lst

if __name__ == "__main__":
	lst = createlist()
	print lst
	print radixsort(lst)