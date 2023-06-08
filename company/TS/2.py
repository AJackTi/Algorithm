dict_ans = dict()

def stockPairs(stocksProfit, target):
    # for i in range(len(stocksProfit)):
    #     for j in range(len(stocksProfit)):
    #         if i != j and stocksProfit[i] + stocksProfit[j] == target and stocksProfit[j] not in dict_ans:
    #             dict_ans[stocksProfit[i]] = stocksProfit[j]
    
    # return len(dict_ans)
    
    stocksProfit = removeDuplicate(stocksProfit, int(target/2))
    dict_ans = dict()
    ans = 0
    for i in range(len(stocksProfit)):
        x = target - stocksProfit[i]
        if x in dict_ans:
            ans += 1
        else:
            dict_ans[stocksProfit[i]] = x
            
    return ans

def removeDuplicate(sliceList, notRemove):
    all_keys = {}
    repetition_dict = {}
    lst = []
    for i in range(len(sliceList)):
        if sliceList[i] in repetition_dict and repetition_dict[sliceList[i]] == 2:
            continue
        
        if sliceList[i] not in all_keys: 
            all_keys[sliceList[i]] = True
            lst.append(sliceList[i])
        elif sliceList[i] == notRemove:
                lst.append(sliceList[i])

        if sliceList[i] not in repetition_dict:
            repetition_dict[sliceList[i]] = 1
        else:
            repetition_dict[sliceList[i]] += 1

    return lst
    
if __name__ == '__main__':
    stocksProfit = [6, 6, 6, 3, 9, 3, 5, 1]
    target = 12

    # stocksProfit = [1, 3, 46, 1, 3, 9]
    # target = 47
    
    print(stockPairs(stocksProfit=stocksProfit, target=target))