# AJack Ti
# 9/12/2017
from random import randint
import math

def create_list():
	return [randint(10,99) for i in range(10)]


def swap(lst, a, b): # a, b: index and a, b
    if a > b:
        a,b = b,a
    lst.insert(a, lst[b])
    lst.insert(b+1, lst[a+1])
    del lst[a+1]
    del lst[b+1]
    return lst

def bucketsort(lst):
	dic = {}
	for i in lst:
		digits = int(math.log10(i))
		if i/(10**digits) in dic.keys():
			# append vao trong list
			dic[i/(10**digits)].append(i)
		else:
			dic.update({i/(10**digits):[i]})
	
	for i in dic.keys():
		if dic[i] <= 1:
			continue
		for j in range(1, len(dic[i])):
			k = j - 1
			if dic[i][j] < dic[i][k]:
				swap(dic[i], j, k)
				j -= 1

	arr_results = []
	for i in dic.values():
		arr_results += i

	return arr_results

if __name__ == "__main__":
    lst = create_list()
    print (lst)
    print (bucketsort(lst))