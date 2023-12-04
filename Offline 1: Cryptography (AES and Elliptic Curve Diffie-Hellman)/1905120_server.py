import socket
import AES
import EC
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections (max 1 connection in this example)
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")


# Generate shared Parameters, private key and public key
g_x, g_y, a, b, P = EC.generate_sharedParameter(nBits=128)
k_pr = EC.generate_privateKey(P)
k_pub_x, k_pub_y = EC.generate_publicKey(g_x, g_y, a, b, P, k_pr)


# Convert numbers to a string and concatenate them
numbers = [g_x, g_y, a, b, P, k_pub_x, k_pub_y ]
string_numbers = ','.join(map(str, numbers))

client_socket.send(string_numbers.encode())

# Receive data from the client
data = client_socket.recv(1024)
s = data.decode()

# Split the string and convert back to numbers
extracted_numbers = list(map(int, s.split(',')))

k_pub_x_B, k_pub_y_B = extracted_numbers



aesKey, _ = EC.generateSharedKey(k_pub_x_B, k_pub_y_B, a, b, P, k_pr)

print("\nGenerated AES by EC(Alice): ", aesKey)

hex_key = AES.str2Hex(str(aesKey))


print("\nInput the message:")
plain_text = input("In ASCII: ")


# ENCRYPTION
init_vector = ['00']*16 

hex_cypertext = AES.CBC_encryption(plain_text, str(aesKey), init_vector)


print("\nCiphered Text:")
AES.printHexStr(hex_cypertext)
message = AES.hex2Str(hex_cypertext)

client_socket.send(message.encode())


# Close the connection
client_socket.close()
server_socket.close()
