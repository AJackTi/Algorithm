package main

import "fmt"

func stockPairs(stocksProfit []int32, target int64) int32 {
	// mapValues := make(map[int32]bool)
	// var ans int32
	// for i := 0; i < len(stocksProfit); i++ {
	// 	if _, isExistI := mapValues[stocksProfit[i]]; !isExistI {
	// 		for j := i+1; j<len(stocksProfit); j++ {
	// 			if stocksProfit[i] + stocksProfit[j] == int32(target) {
	// 				_, isExistI := mapValues[stocksProfit[i]]
	// 				_, isExistJ := mapValues[stocksProfit[j]]
	
	// 				if !isExistI && !isExistJ {
	// 					mapValues[stocksProfit[i]] = true
	// 					mapValues[stocksProfit[j]] = true
	// 					ans++
	// 					break
	// 				}
	// 			}
	// 		}
	// 	}
	// }

	// return ans

	dic := make(map[int64]int64)
	var ans int32
	stocksProfit = removeDuplicate(stocksProfit, int32(target/2)) // re-assign
	for _, num := range stocksProfit {
		x := target - int64(num)
		_, ok := dic[x]
		if ok {
			ans++
		} else {
			dic[int64(num)] = x
		}
	}

	return ans
}

func removeDuplicate[T int32](sliceList []T, notRemove T) []T {
    allKeys := make(map[T]bool)
	repetitionMap := make(map[T]int)
    list := []T{}
    for _, item := range sliceList {
		if repetition, _ := repetitionMap[item]; repetition == 2 {
			continue
		}
		
		if _, value := allKeys[item]; !value {
			allKeys[item] = true
			list = append(list, item)
		} else if item == notRemove {
			list = append(list, item)
		}
		repetitionMap[item] += 1
    }
    return list
}

func main() {
	// var stocksProfit []int32 = []int32{1, 3, 46, 1, 3, 9}
    // var target int64 = 47
	
	// var stocksProfit []int32 = []int32{92, 407, 1152, 403, 1419, 689, 1029, 108, 128, 1307, 300, 775, 622, 730, 978, 526, 943, 127, 566, 869, 715, 983, 820, 1394, 901, 606, 497, 98, 1222, 843, 600, 1153, 302, 1450, 1457, 973, 1431, 217, 936, 958, 1258, 970, 1155, 1061, 1341, 657, 333, 1151, 790, 101, 588, 263, 101, 534, 747, 405, 585, 111, 849, 695, 1256, 1508, 139, 336, 1430, 615, 1295, 550, 783, 575, 992, 709, 828, 1447, 1457, 738, 1024, 529, 406, 164, 994, 1008, 50, 811, 564, 580, 952, 768, 863, 1225, 251, 1032, 1460}
    // var target int64 = 1558
	
	var stocksProfit []int32 = []int32{6, 6, 3, 9, 3, 5, 1, 6}
    var target int64 = 12

	stockPairs := stockPairs(stocksProfit, target)

	fmt.Println(stockPairs) 
}