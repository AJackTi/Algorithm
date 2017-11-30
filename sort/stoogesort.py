# AJack Ti
# 30/11/2017

# -*- coding: utf-8 -*-
from random import randint

def create_list():
	return [randint(1,20) for i in range(20)] 

def stoogesort(L, i=0, j=None):
	if j is None:
		j = len(L) - 1
	if L[j] < L[i]:
		L[i], L[j] = L[j], L[i]
	if j - i > 1:
		t = (j - i + 1) // 3
		stoogesort(L, i  , j-t)
		stoogesort(L, i+t, j  )
		stoogesort(L, i  , j-t)
	return L
if __name__ == "__main__":
	lst = create_list()
	print lst
	print stoogesort(lst,0)