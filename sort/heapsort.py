# 21/11/2017
# AJack Ti

# -*- coding: utf-8 -*-
from random import randint

def create_list():
	return [randint(1,20) for i in range(20)]

def heapsort(lst):
	count = 0
	lst_temp = [] # contain elements max of lst
	# list này chứa các phần tử max khi mà nó so sánh đến node cha

	while len(lst) > 0:
		for i in reversed(range(len(lst)/2)):
			"""
			# => parent=2*i/2 left=2*i right=2*i+1
			"""
			parent = 2*i/2
			left = 2*i+1
			right = 2*i+2
			max_sub = 0
			if right >= len(lst):
				max_sub = lst[left]
			else:
				max_sub = max(lst[left], lst[right])
			if lst[parent] < max_sub:
				# To define index of node parent and node max
				# Xác định index của node cha và node max(2 node con) => insert và xóa 
				index_max = lst.index(max_sub)
				lst.insert(parent, max_sub)
				lst.insert(index_max+1, lst[parent+1])
				del lst[i+1]
				del lst[index_max+1]
		lst_temp.append(lst.pop(0))

	return lst_temp

if __name__ == "__main__":
	lst = create_list()
	print heapsort(lst)