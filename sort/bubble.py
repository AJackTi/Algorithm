# 16/11/2017
# Author: AJackTi

from random import randint

def createlist():
	lst = []

	for i in range(10):
		lst.append(randint(0,20))
	return lst

def transfer(lst, i, j):
	lst.insert(j,lst[i])
	lst.insert(i+1,lst[j+1])
	del lst[j+1]
	del lst[i+1]

def bubble(lst):
	temp = 0
	while temp < len(lst):
		for i,j in zip(reversed(range(temp+1,len(lst))), reversed(range(temp,len(lst)-1))):
			if lst[i] < lst[j]:
				transfer(lst, i, j)
				print lst
		temp += 1
	return lst

if __name__ == "__main__":
	lst = createlist()
	print bubble(lst)
		