from random import randint

def linear_search(x, lst):
	for i in range(len(lst)):
		if x == lst[i]:
			return i
	return -1

def create_list():
	return [randint(1,20) for i in range(20)]

if __name__ == "__main__":
	lst = create_list()
	print(lst)
	if linear_search(10, lst) != -1:
		print(linear_search(10, lst))
	else:
		print("Not Found")