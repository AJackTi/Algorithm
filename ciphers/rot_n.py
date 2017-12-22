import string
from optparse import OptionParser

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase

def parse():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                  help="Type input want to encrypt", metavar="string")
    parser.add_option("-r", "--rot", dest="rot",
                  help="Type rot n", metavar="int")

    (options, args) = parser.parse_args()

    if int(options.rot) not in range(0,26):
        parser.error("Incorrect rot n")
    
    return options.input, options.rot

def rotn_encrypt(input, n):
    str_result = ""
    for char in input:
        if char in UPPERCASE:
            if ( ord(char) + n ) > 90:
                str_result += chr( 64 + (ord(char) + n ) - 90 ) 
            else:
                str_result += chr( ord(char) + n )
        elif char in LOWERCASE:
            if ( ord(char) + n ) > 122:
                str_result += chr( 96 + (ord(char) + n) - 122)
            else:
                str_result += chr( ord(char) + n )
        else:
            str_result += char
    return str_result

def rotn_decrypt(input, n):
    str_result = ""
    for char in input:
        if char in LOWERCASE:
            if ( ord(char) - n ) < 97:
                str_result += chr( ord(char) - n + 26)
            else:
                str_result += chr( ord(char) - n)
        elif char in UPPERCASE:
            if ( ord(char) - n ) < 65:
                str_result += chr( ord(char) - n + 26)
            else:
                str_result += chr( ord(char) - n)
        else:
            str_result += char
    
    return str_result
            
if __name__ == "__main__":
    # Usage: python rot_n.py -r 1 -i "Hello"
    input, rot = parse()
    rot = int(rot)
    print rotn_encrypt(input, rot)
    print rotn_decrypt( rotn_encrypt(input, rot), rot )