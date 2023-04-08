A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 3]

def is_rotation(A, B):
    if len(A) == len(B):
        try:
            index = B.index(A[0])
        except:
            return False
        return B[index:] + B[:index] == A
    else:
        return False

list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
list2b = [4, 5, 6, 7, 1, 2, 3]
list2c = [4, 5, 6, 9, 1, 2, 3]
list2d = [4, 6, 5, 7, 1, 2, 3]
list2e = [4, 5, 6, 7, 0, 2, 3]
list2f = [1, 2, 3, 4, 5, 6, 7]

# print(is_rotation(A, B))
print(is_rotation(list1, list2b))