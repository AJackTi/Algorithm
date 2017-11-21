# 15/11/2017
# Author: AJackTi

from random import randint

lst = []

for i in range(10):
	lst.append(randint(1,20))

print lst

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
	if len(lst) == 1:
		print lst
	else:
		print selection(lst)