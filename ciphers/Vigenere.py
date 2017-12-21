# 21/12/2017
# AJack Ti
from optparse import OptionParser
import string
from random import randint

def parse():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input",
                  help="Type input want to encrypt", metavar="string")
    parser.add_option("-k", "--key", dest="key",
                  help="Type key", metavar="string")
    (options, args) = parser.parse_args()

    if any(char.isdigit() for char in options.key) or any(char.isdigit() for char in options.input):
        parser.error("incorrect key or input")
    if len(str(options.key)) == 0 or len(str(options.key)) == 0:
        parser.error("incorrect key or input")
    if ' ' in options.key or ' ' in options.input:
        parser.error("incorrect key or input")
        
    options.key = options.key.upper()
    options.input = options.input.upper()

    if len(options.key) < len(options.input):
        while len(options.key) < len(options.input):
            options.key += options.key[:len(options.input)-len(options.key)]

    return options.input, options.key

def process(lst_input, lst_key):
    lst_result = []
    for i,j in zip(lst_input, lst_key):
        if (ord(i) + abs((ord('A') - ord(j)))) > 90:
            lst_result.append( chr(ord(i) + abs((ord('A') - ord(j))) - 26) )
        else:
            lst_result.append( chr(ord(i) + abs((ord('A') - ord(j)))) )
    return lst_result

def string_to_list(input):
    return [i for i in input]

def list_to_string(input):
    return "".join(i for i in input)

def lowercase_to_uppercase(input):
    return chr(ord(input) - 32)


if __name__ == "__main__":
    str_input, str_key = parse()
    print "With input: " + str_input
    print "And key: " + str_key
    print list_to_string(process(string_to_list(str_input), string_to_list(str_key)))