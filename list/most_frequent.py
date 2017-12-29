lst = [1, 3, 1, 3, 2, 1]
# # C1:
# from collections import Counter

# def Most_Common(lst):
#     data = Counter(lst)
#     return data.most_common(1)[0][0]

# # C2:
# def most_common (lst):
#     return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

# print most_common([1, 3, 1, 3, 2, 1])

# C3: Use Hash Map
# arr = [[] for i in range(0, 10)]

# for item in lst:
#     arr[item%10].append([item%10])

# print max(((item, lst.count(item)) for item in set(set(lst))), key=lambda a: a[1])[0]

# C4:
import operator

dict_count = {}

for item in set(lst):
    dict_count.update( {item:lst.count(item)} )

print max(dict_count.iteritems(), key=operator.itemgetter(1))[0]