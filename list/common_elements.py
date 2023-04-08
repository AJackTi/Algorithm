A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]

# C1:
# print([i for i in A if i in B])

# C2:
# print(list(set(A).intersection(B)))

# C3:
# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))

# print(common_elements(A, B))

# C4:
# commonalities = set(A) - (set(A) - set(B))
# print(list(commonalities))
