# source: https://www.youtube.com/watch?v=qjvx0Ge7aos
from random import randint

def create_list():
	return [randint(1,20) for i in range(20)]

k = 0

def Quicksort(lst, right, left):
	if (left < right):
		k = Partition(lst, right, left)
		Quicksort(lst, k-1, left)
		Quicksort(lst, right, k+1)
	else:
		return lst

def Partition(lst, right, left):
	x = lst[left]
	i = left + 1
	j = right
	
	while i <= j:
		while (i<=j) and (lst[i]<=x):
			i += 1
		while (i<=j) and (lst[j]>x):
			j -= 1
		if i < j:
			lst.insert(i, lst[j])
			lst.insert(j+1, lst[i+1])
			del lst[i+1]
			del lst[j+1]
			i += 1
			j -= 1

	lst.insert(left, lst[j])
	lst.insert(j+1, lst[left+1])
	del lst[left+1]
	del lst[j+1]
	
	return j
	# return lst

if __name__ == "__main__":
	lst = create_list()
	print (lst)
	left = 0
	right = len(lst)-1
	Quicksort(lst, right, left)
	print (lst)