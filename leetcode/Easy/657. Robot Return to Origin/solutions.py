def judgeCircle(moves: str) -> bool:
    dict_ans = {}
    for i in moves:
        if i not in dict_ans:
            dict_ans[i] = 0
        else:
            dict_ans[i] += 1
    
    if len(dict_ans) % 2 == 1:
        return False
        
    if ('L' in dict_ans and 'R' in dict_ans) and ('U' in dict_ans and 'D' in dict_ans):
        return dict_ans['L'] == dict_ans['R'] and dict_ans['U'] == dict_ans['D']
    
    if 'U' in dict_ans and 'D' in dict_ans:
        return dict_ans['U'] == dict_ans['D']
    
    if 'U' in dict_ans and 'D' in dict_ans:
        return dict_ans['U'] == dict_ans['D']
    
    return False
    
# moves = "UD"
# moves = "LL"
moves = "DURDLDRRLL"
print(judgeCircle(moves=moves))