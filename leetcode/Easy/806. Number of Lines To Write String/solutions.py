def numberOfLines(widths: list[int], s: str) -> list[int]:
    result = [1, 0]
    for c in s:
        w = widths[ord(c)-ord('a')]
        result[1] += w
        if result[1] > 100:
            result[0] += 1
            result[1] = w
    return result


widths = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
s = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
print(numberOfLines(widths, s))