def sortArrayByParity(nums: list[int]) -> list[int]:
    lst_even = []
    lst_odd = []
    for i in sorted(nums):
        if i % 2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
            
    return lst_even + lst_odd

nums = [3,1,2,4]
print(sortArrayByParity(nums=nums))