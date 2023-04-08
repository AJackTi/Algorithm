def restoreString(s: str, indices: list[int]) -> str:
    dict_indices = {}
    for index, value in enumerate(indices):
        dict_indices[value] = s[index]
    
    sorted_dict = {k:v for k,v in sorted(dict_indices.items())}
    result = ""
    for k, v in sorted_dict.items():
        result += v
        
    return result

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))