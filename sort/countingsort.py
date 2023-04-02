# AJack Ti
# 7/12/2017

from random import randint
import math
# -*- coding: utf-8 -*-

def createlist():
	lst = []

	for i in range(20):
		lst.append(randint(0,900))
	return lst

def countingsort(lst):
    digits = int(math.log10(max(lst)))+1
    lst_add = [0 for i in range(0,10**digits)]
    j = 0 # index
    while j < 10**digits:
        for i in lst:
            if i == j:
                lst_add[j] += 1
        j += 1
        
    for i in range(1, len(lst_add)):
        j = i - 1
        lst_add.insert(i, lst_add[i]+lst_add[j])
        del lst_add[i+1]

    lst_result = [0 for i in range(0,len(lst))]

    for i in lst:
        index = lst_add[i]
        lst_result.insert(index-1, i)
        del lst_result[index]
        lst_add[i] -= 1

    return lst_result


if __name__ == "__main__":
    lst = createlist()
    print (lst)
    # lst = [9,8,7,6,5,3,2,1]
    print (countingsort(lst))
