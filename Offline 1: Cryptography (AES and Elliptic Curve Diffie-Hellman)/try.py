import random
import AES

# Generate a random 16-bit string
random_16_bit_string = ''.join(chr(random.randint(33, 126)) for _ in range(16))

print(random_16_bit_string)

str_hex = AES.str2Hex(random_16_bit_string)

AES.printHexStr(str_hex)