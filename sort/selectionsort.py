# 15/11/2017
# Author: AJackTi

from random import randint

def create_list():
	return [randint(1,20) for i in range(20)]

def selection(lst):
	i = 0
	while True:
		minimum = min(lst[i:])
		index = lst[i:].index(minimum)
		lst.insert(i,minimum)
		del lst[index + 1 + i]
		i += 1
		if i == len(lst):
			return lst

if __name__ == "__main__":
	lst = create_list()
	print lst
	if len(lst) == 1:
		print lst
	else:
		print selection(lst)