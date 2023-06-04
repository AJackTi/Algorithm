package main

import "fmt"

func performOperations(arr []int32, operations [][]int32) []int32 {
	for _, value := range operations {
		reverse(arr[value[0]: value[1]+1])
	}

	return arr
}

func reverse[S ~[]E, E any](s S) S {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func main() {
	operations := [][]int32{{0, 9}, {4, 5}, {3, 6}, {2, 7}, {1, 8}, {0, 9}}
	arr := []int32{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
	result := performOperations(arr, operations)
	fmt.Println(result)
}
