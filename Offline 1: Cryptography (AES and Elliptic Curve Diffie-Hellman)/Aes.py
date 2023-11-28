

def str2Hex(str):
    hex_str= []

    for i in range(len(str)):
        hex_value = hex(ord(str[i]))[2:].zfill(2)  # Remove '0x' and zero-pad
        hex_str.append(hex_value)

    while(len(hex_str)%16 != 0):
        hex_str.append('00')
    
    return hex_str

def printHexStr(hex_arr):
    print("In HEX: ", end="")

    for i in range(len(hex_arr)):
        print(hex_arr[i], end=" ")

    print()



print("Key:")
# key = input("In ASCII: ")
key = "BUET CSE19 Batch"

if(len(key) < 16):
    #  make the key 16 byte length
    key = key.ljust(16, '0')

print(key)

# Convert key into hex array and print as well
hex_key = str2Hex(key)
printHexStr(hex_key)

print("\nPlain Text:")
# plain_text = input("In ASCII: ")
plain_text = "Never Gonna Give you up"

# Convert plaint_text into hex array and print as well
hex_plain_text = str2Hex(plain_text)
printHexStr(hex_plain_text)

# print(type(hex_plain_text[0]))  # str type

