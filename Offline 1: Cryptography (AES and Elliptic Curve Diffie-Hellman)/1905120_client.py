import socket
import importlib

AES = importlib.import_module("1905120_AES")
EC = importlib.import_module("1905120_EC")

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
print(f"Connected to {host}:{port}")

# Receive the welcome message from the server
message = client_socket.recv(1024)
s = message.decode()

# Split the string and convert back to numbers
extracted_numbers = list(map(int, s.split(',')))

g_x, g_y, a, b, P, k_pub_x_A, k_pub_y_A  = extracted_numbers

# Generate private key and public key

k_pr = EC.generate_privateKey(P)
k_pub_x, k_pub_y = EC.generate_publicKey(g_x, g_y, a, b, P, k_pr)

# Convert numbers to a string and concatenate them
numbers = [ k_pub_x, k_pub_y ]
string_numbers = ','.join(map(str, numbers))

client_socket.send(string_numbers.encode())



aesKey, _ = EC.generateSharedKey(k_pub_x_A, k_pub_y_A, a, b, P, k_pr)

print("\bGenerated AES by EC(Bob) : ", aesKey)

hex_key = AES.str2Hex(str(aesKey))


# receiving init_string
message = client_socket.recv(1024)
random_init_string = message.decode()

# print(random_init_string)

init_vector = AES.str2Hex(random_init_string)

message = client_socket.recv(1024)
received_message = message.decode()

hex_cypertext = AES.str2Hex(received_message)

print("\nReceived Cyper Text: ")
AES.printHexStr(hex_cypertext)

hex_decrypted = AES.CBC_decryption(hex_cypertext, str(aesKey), init_vector)

print("\nRecived message after decryption: ")
AES.printHexStr(hex_decrypted)
message = AES.hex2Str(hex_decrypted)
print("In ASCII: ", end="")
print(message)

# Close the connection
client_socket.close()
