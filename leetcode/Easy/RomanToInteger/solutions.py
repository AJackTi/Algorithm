dictDefined = {
                "I": 1,
                "IV": 4,
                "V": 5,
                "IX": 9,
                "X": 10,
                "XL": 40,
                "L": 50,
                "XC": 90,
                "C": 100,
                "CD": 400,
                "D": 500,
                "CM": 900,
                "M": 1000
                }

def romanToInt(s):
    list = [i for i in s]
    dict = {}
    total = 0
    index = 0
    while index < len(list):
        value = list[index]
        if value == "I" and (index != len(list) - 1 and list[index + 1] == "V"):
            total += 4
            index += 2
            continue
        if value == "I" and (index != len(list) - 1 and list[index + 1] == "X"):
            total += 9
            index += 2
            continue
        if value == "X" and (index != len(list) - 1 and list[index + 1] == "L"):
            total += 40
            index += 2
            continue
        if value == "X" and (index != len(list) - 1 and list[index + 1] == "C"):
            total += 90
            index += 2
            continue
        if value == "C" and (index != len(list) - 1 and list[index + 1] == "D"):
            total += 400
            index += 2
            continue
        if value == "C" and (index != len(list) - 1 and list[index + 1] == "M"):
            total += 900
            index += 2
            continue
        
        if value not in dict:
            dict[value] = 1
        else:
            dict[value] += 1
        
        index += 1
    
    for k in dict.keys():
        total += dict[k] * dictDefined[k]

    return total

print(romanToInt("MCMXCIV"))
print(romanToInt("III"))
print(romanToInt("LVIII"))