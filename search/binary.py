# -*- coding: utf-8 -*-
"""
# Điều kiện quyết định cho thuật toán này là: LIST PHẢI ĐƯỢC SẮP XẾP.
# Ta phải sắp xếp nó đầu tiên nếu không thuật toán sẽ hoạt động không đúng.
"""
def binary_search(x, mid, left, right, lst):
    if left > right: # Không tìm thấy phần tử trong list này. 
        return -1
    if lst[mid] == x:
        return mid
    elif x > lst[mid]:
        return binary_search(x, (left+right)//2, mid+1, right, lst)
    elif x < lst[mid]:
        return binary_search(x, (left+right)//2, left, mid-1, lst)

if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9,10]
    mid = len(lst) // 2
    left = 0
    right = len(lst)-1
    if binary_search(2, mid, left, right, lst) == -1:
        print("Not Found")
    else:
        print(binary_search(2, mid, left, right, lst))
