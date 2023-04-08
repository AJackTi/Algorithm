import string

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase

def rot13_encrypt(input):
    str_result = ""
    for char in input:
        if char in UPPERCASE:
            if ( ord(char) + 13 ) > 90:
                str_result += chr( 64 + (ord(char) + 13 ) - 90 ) 
            else:
                str_result += chr( ord(char) + 13 )
        elif char in LOWERCASE:
            if ( ord(char) + 13 ) > 122:
                str_result += chr( 96 + (ord(char) + 13) - 122)
            else:
                str_result += chr( ord(char) + 13 )
        else:
            str_result += char
    return str_result

def rot13_decrypt(input):
    str_result = ""
    for char in input:
        if char in UPPERCASE:
            if ( ord(char) - 13 ) < 65:
                str_result += chr( ord(char) - 13 + 26)
            else:
                str_result += chr( ord(char) - 13 )
        elif char in LOWERCASE:
            if ( ord(char) - 13 ) < 97:
                str_result += chr( ord(char) - 13 + 26)
            else:
                str_result += chr( ord(char) - 13 )
        else:
            str_result += char
    return str_result

if __name__ == "__main__":
    input = LOWERCASE + UPPERCASE
    print(input)
    print(rot13_encrypt(input))
    print(rot13_decrypt( rot13_encrypt(input) ))