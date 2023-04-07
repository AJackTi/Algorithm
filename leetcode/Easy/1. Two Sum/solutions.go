package main

import "fmt"

func twoSum(nums []int, target int) []int {
	dic := map[int]int{}
	for index, num := range nums {
		x := target - num
		val, ok := dic[x]
		if ok {
			return []int{val, index}
		}
		dic[num] = index
	}

	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
