# AJack Ti
# 30/11/2017
from random import randint

def create_list():
	return [randint(1,20) for i in range(20)]

def compare_list(lst1, lst2):
	if not lst1 and lst2:
		return lst2
	elif not lst2 and lst1:
		return lst1
	elif not lst1 and not lst2:
		return []
	i,j = 0,0
	arr = []
	while True:
		if lst1[i] < lst2[j]:
			arr.append(lst1[i])
			i += 1
		else:
			arr.append(lst2[j])
			j += 1

		if i == len(lst1):
			return arr + lst2[j:]
		if j == len(lst2):
			return arr + lst1[i:]

def merge_sort(lst):
	arr = [lst[0]]
	for i in range(1, len(lst)):
		lst_merge = compare_list(arr, [lst[i]])
		arr = []
		arr += lst_merge
		
	return arr

if __name__ == "__main__":
	lst = create_list()
	print lst
	print merge_sort(lst)