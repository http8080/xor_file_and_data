import binascii
import sys


# xor 연산 시 길이를 맞추기 위해서 필요
def padding_xor(string, sinput):
    if len(string) > len(sinput):
        sinput='0' * (len(string) - len(sinput)) + sinput
    elif len(sinput) > len(string):
        string='0' * (len(sinput) - len(string)) + string
    if len(string) % 2 != 0:
        string='0' + string
    if len(sinput) % 2 != 0:
	    sinput='0' + sinput

    return string, sinput


# hex 값으로 리턴
def unhexlify(data):
    return binascii.unhexlify("0b" + data)


def hexlify(data):
    return binascii.hexlify(data)


# 마지막 XOR 연산 후 리턴
def xor_strings(string, sinput):
    result = ""
    for x, y in zip(string, sinput):
        result += chr(x ^ y)
    
    return result.encode()


string = sys.argv[1]
signature = sys.argv[2]

string, sinput = padding_xor(string, signature)

string = unhexlify(string)
sinput = unhexlify(sinput)

print(hexlify(xor_strings(string, sinput)))