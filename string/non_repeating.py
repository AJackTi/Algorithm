str = "aabcbdefgh"
lst = list(str)

# use set:
for i in [(item, lst.count(item)) for item in set(lst)]:
    if i[1] == 1:
		print i[0],

# use dictionary:
for element in [{item: lst.count(item)} for item in lst]:
    if element.values() == [1]:
        print element.keys(),