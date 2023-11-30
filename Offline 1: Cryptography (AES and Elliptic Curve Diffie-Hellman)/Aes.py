from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


def str2Hex(str):
    hex_str= []

    for i in range(len(str)):
        hex_value = hex(ord(str[i]))[2:]  # str -> unicode -> hex -> Remove '0x'
        hex_str.append(hex_value)

    while(len(hex_str)%16 != 0):
        hex_str.append('00')
    
    return hex_str

def hex2Str(hex_str):
    result_str = ''

    for hex_value in hex_str:
        char = chr(int(hex_value, 16))
        result_str += char

    return result_str


def printHexStr(hex_arr):
    print("In HEX: ", end="")

    for i in range(len(hex_arr)):
        print(hex_arr[i], end=" ")

    print()

def xorHex(a_hex, b_hex):

    a = BitVector(hexstring=a_hex)
    b = BitVector(hexstring=b_hex)

    
    # Convert hexadecimal strings to integers
    int_a = a.intValue()
    int_b = b.intValue()

    # bitwise x-or
    result = int_a ^ int_b

    # Convert the result back to hexadecimal and remove the '0x' prefix
    result_hex = BitVector(intVal=result, size=8).get_bitvector_in_hex()

    return result_hex

def xorTwoWords(w1, w2):
    r_w = []

    for i in range(len(w1)):
        r_w.append(xorHex(w1[i], w2[i]))

    return r_w


def circularByteLeftShift(w):

    cir_w = []

    for i in range(1, len(w)):
        cir_w.append(w[i])

    cir_w.append(w[0])

    return cir_w

def substituteBytes(w):
    bs_w = []

    for i in range(len(w)):
        b = BitVector(hexstring=w[i])
        int_val = b.intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        bs_w.append(s.get_bitvector_in_hex())

    return bs_w

    
def addRoundConstant(w, r):

    rc_i = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']
    # rc_i = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    
    rcon = [rc_i[r-1]]
    a = rcon + ['00', '00', '00', '00']
    # a = rcon + [0x00, 0x00, 0x00 , 0x00]

    arc_w = []

    for i in range(len(w)):
        arc_w.append(xorHex(w[i], a[i]))

    return arc_w
    
def g(w, r):
    cir_w = circularByteLeftShift(w)
    byte_w = substituteBytes(cir_w)
    g_out = addRoundConstant(byte_w, r)

    return g_out

def getNextRoundKey(w, r):

    # Split w into w0, w1, w2, w3
    w0, w1, w2, w3 = w[:4], w[4:8], w[8:12], w[12:16]

    g_w = g(w3, r)
    w4 = xorTwoWords(w0, g_w)
    w5 = xorTwoWords(w4, w1)
    w6 = xorTwoWords(w5, w2)
    w7 = xorTwoWords(w6, w3)

    # Concatenate w4, w5, w6, w7 to form n_w
    n_w = w4 + w5 + w6 + w7

    return n_w


def expandKeys(hex_key):

    roundKeys = []

    roundKeys.append(hex_key)


    for i in range(10):
        roundKeys.append(getNextRoundKey(roundKeys[i], i+1))

    # print(roundKeys)
    return roundKeys


def list2matrix(w):
    matrix = [[0] * 4 for _ in range(4)]

    for col in range(4):
        for row in range(4):
            matrix[row][col] = w[col*4 + row] 

    return matrix

def matrix2list(matrix):
    l = []

    for col in range(4):
        for row in range(4):
            l.append(matrix[row][col])

    return l

def addRoundKey(message, key):
    matrix = []

    for r in range(4):
        row = []
        for c in range(4):
            row.append(xorHex(message[r][c], key[r][c]))
        matrix.append(row)
    
    return matrix
            

def substituteByteMatrix(w, isEncryption):
    bs_matrix = []

 
    for r in range(4):
        row = []
        for c in range(4):
            b = BitVector(hexstring=w[r][c])
            int_val = b.intValue()

            if isEncryption:
                s = Sbox[int_val]
            else:
                s = InvSbox[int_val]

            s = BitVector(intVal=s, size=8)
            row.append(s.get_bitvector_in_hex())
        bs_matrix.append(row)
 

    return bs_matrix

def circularLeftShift(w, shift_amount):
    cir_w = w[shift_amount:] + w[:shift_amount]
    return cir_w

def shiftRow(w):
    s_w = []

    for i in range(4):
        s_w.append(circularLeftShift(w[i], i))

    return s_w

def circularRightShift(w, shift_amount):
    cir_w = w[-shift_amount:] + w[:-shift_amount]
    return cir_w

def invShiftRow(w):
    s_w = []

    for i in range(4):
        s_w.append(circularRightShift(w[i], i))

    return s_w

def mixColumn(w, isEncryption):

    result = [[BitVector(intVal=0, size=8) for _ in range(4)] for _ in range(4)]

    AES_modulus = BitVector(bitstring='100011011')

    for i in range(4):
        for j in range(4):
            for k in range(4):
                
                b = BitVector(hexstring=w[k][j])

                # BitVector multiplicatiion instead of multiplication
                if isEncryption:
                    product = Mixer[i][k].gf_multiply_modular(b, AES_modulus, 8)
                else:
                    product = InvMixer[i][k].gf_multiply_modular(b, AES_modulus, 8)

                # Bitwise XOR instead of addition
                result[i][j] ^= product
    
    for i in range(4):
        for j in range(4):
            result[i][j] = result[i][j].get_bitvector_in_hex()

    return result

def blockEncrypt(hex_message, key):
    
    message_mat = list2matrix(hex_message)

    hex_key = str2Hex(key)
    key_mat = list2matrix(hex_key)


    #INITIAL ROUND
    # Key Expansion - initially done
    

    #Add Round key
    state_mat = addRoundKey(message_mat, key_mat)

    #MAIN BODY (9 ROUNDS)
    for i in range(1, 10):
        state_mat = substituteByteMatrix(state_mat, 1)

        state_mat = shiftRow(state_mat)

        state_mat = mixColumn(state_mat, 1)

        key_mat_round = list2matrix(roundkeys[i])
        state_mat = addRoundKey(state_mat, key_mat_round)
    
    #FINAL ROUND
    state_mat = substituteByteMatrix(state_mat, 1)
    state_mat = shiftRow(state_mat)
    key_mat_final = list2matrix(roundkeys[10])
    encrypted_mat = addRoundKey(state_mat, key_mat_final)

    cypertext = matrix2list(encrypted_mat)

    return cypertext


def blockDecrypt(cypertext, key):

    hex_key = str2Hex(key)
    # hex_cyper_text = str2Hex(message)
    hex_cyper_text = cypertext
    cyper_mat = list2matrix(hex_cyper_text)

    #INITIAL ROUND
    # Key Expansion - initially done

    key_mat = list2matrix(roundkeys[10])

    state_mat = addRoundKey(cyper_mat, key_mat)
    state_mat = invShiftRow(state_mat)
    state_mat = substituteByteMatrix(state_mat, 0)

    #MAIN BODY (9 ROUNDS)
    for i in range(1, 10):
        key_mat_round = list2matrix(roundkeys[10-i])
        state_mat = addRoundKey(state_mat, key_mat_round)
        
        state_mat = mixColumn(state_mat, 0)

        state_mat = invShiftRow(state_mat)

        state_mat = substituteByteMatrix(state_mat, 0)

    #FINAL ROUND
    key_mat_final = list2matrix(roundkeys[0])
    encrypted_mat = addRoundKey(state_mat, key_mat_final)

    message = matrix2list(encrypted_mat)

    return message



def split_into_blocks(hex_plain_text, block_size=16):

    # Split the hex_plain_text into blocks
    blocks = [hex_plain_text[i:i+block_size] for i in range(0, len(hex_plain_text), block_size)]

    return blocks


def CBC_encryption(message, key, init_vector):
    
    hex_plain_text = str2Hex(message)
    # divide hex_plain_text into blocks of each 16 elements. hex_plain_text is gauranteed to be in multiple of 16

    hex_plaintext_blocks = split_into_blocks(hex_plain_text)

    hex_cypertext = []

    for i in range(len(hex_plaintext_blocks)):

        text = xorTwoWords(hex_plaintext_blocks[i], init_vector)

        cypertext = blockEncrypt(text, key)

        hex_cypertext += cypertext

        init_vector = cypertext

    return hex_cypertext

def CBC_decryption(hex_cypertext, key, init_vector):
    
    hex_cypertext_blocks = split_into_blocks(hex_cypertext)

    hex_decryted = []

    for i in range(len(hex_cypertext_blocks)):

        hex_temp = blockDecrypt(hex_cypertext_blocks[i], key)

        hex_message = xorTwoWords(hex_temp, init_vector)

        hex_decryted += hex_message

        init_vector = hex_cypertext_blocks[i]

    return hex_decryted






print("Key:")
key = input("In ASCII: ")
# key = "BUET CSE19 Batch"

# Convert key into hex array, add 00 as padding, take first 16 bytes and print as well
hex_key = str2Hex(key)
hex_key = hex_key[:16]
printHexStr(hex_key)


print("\nPlain Text:")
plain_text = input("In ASCII: ")
# plain_text = "Never Gonna Give you up"

# Convert plaint_text into hex array and print as well
hex_plain_text = str2Hex(plain_text)
printHexStr(hex_plain_text)



#EXPAND KEYS
start_time = time.time()
roundkeys = expandKeys(hex_key)
time_keySchedule = (time.time() - start_time) * 1000


# ENCRYPTION
init_vector = ['00']*16 

start_time = time.time()
hex_cypertext = CBC_encryption(plain_text, key, init_vector)
time_encryption = (time.time() - start_time) * 1000

print("\nCiphered Text:")
printHexStr(hex_cypertext)
message = hex2Str(hex_cypertext)
print("In ASCII: ", end="")
print(message)


# DECRYPTION
init_vector = ['00']*16 

start_time = time.time()
hex_decrypted = CBC_decryption(hex_cypertext, key, init_vector)
time_decryption = (time.time() - start_time) * 1000

print("\nDiciphered Text")
printHexStr(hex_decrypted)
message = hex2Str(hex_decrypted)
print("In ASCII: ", end="")
print(message)


print("\nExecution Time Details:")
print("Key Schedule Time: ", time_keySchedule, " ms")
print("Encryption Time: ", time_encryption, " ms")
print("Decryption Time: ", time_decryption, " ms")

