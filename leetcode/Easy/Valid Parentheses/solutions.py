dictParentheses = {
    "(":")",
    "{":"}",
    "[":"]",
}

def isValid(s: str) -> bool:
    stack = []
    openChars = ['(', '[', '{']
    closeChars = [')', ']', '}']

    if len(s) == 0:
        return True
    
    for i in list(s):
        if i in openChars:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if openChars.index(top) != closeChars.index(i):
                return False

    return len(stack) == 0

print(isValid('()'))