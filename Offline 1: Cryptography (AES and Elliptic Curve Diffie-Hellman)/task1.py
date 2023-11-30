

from BitVector import *

def str2Hex(str):
    hex_str= []

    for i in range(len(str)):
        hex_value = hex(ord(str[i]))[2:].zfill(2)  # Remove '0x' and zero-pad
        hex_str.append(hex_value)

    while(len(hex_str)%16 != 0):
        hex_str.append('00')
    
    return hex_str