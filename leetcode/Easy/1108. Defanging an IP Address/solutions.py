def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')

address = "1.1.1.1"
output = defangIPaddr(address=address)
print(output)