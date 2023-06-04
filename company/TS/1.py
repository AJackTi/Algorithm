

def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr

def performOperations(operations: list[int], arr: list[int]) -> None:
    for i in range(len(operations)):
        arr[operations[i][0]: operations[i][1]+1] = reverse_list(arr[operations[i][0]: operations[i][1]+1])
    

if __name__ == '__main__':
    operations = [[0, 9], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]
    arr = [9,8,7,6,5,4,3,2,1,0]

    performOperations(operations, arr)
    print(arr)