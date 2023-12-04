from Crypto.Random import random
from Crypto.Util import number
from tabulate import tabulate
import time


def generate_P(nBits):
    random_p = number.getPrime(nBits)
    return random_p

def generate_a(P):
     # Generate a random number between 2 and P-1
    a = random.randint(2, P - 1)
    return a

def generate_b(a, P):

    while True:
        # Generate a random number b between 2 and P-1
        b = random.randint(2, P - 1)

        # Check if 4a^3 + 27*b^2 ≡ 0 (mod P)
        if (4 * pow(a, 3, P) + 27*pow(b, 2, P)) % P != 0:
            return b
    


def generate_G(a, b, P):

    # generate y_square = x^3 + ax + b 
    # check if y_square is perfect square
    # if perfect_square return y = square root of y_square else repeat
    while True:

        g_x = random.randint(2, P - 1)

        # Compute y_square = x^3 + ax + b
        y_square = (pow(g_x, 3) + a * g_x + b) % P

        if pow(y_square, (P-1)//2, P) == 1: # Fermat's Thm
            g_y = pow(y_square, (P-1)//4, P)
            return g_x, g_y
  

def point_addition(x1, y1, x2, y2, a, b, P):
    s = ((y2-y1)*number.inverse(x2-x1, P)) % P
    x3 = (s**2 - x1 - x2) % P
    y3 = (s*(x1-x3) - y1) % P

    return x3, y3

def point_doubling(x1, y1, a, b, P):
    s = ((3*(x1**2)+a)*number.inverse(2*y1, P)) % P
    x3 = (s**2 - x1 - x1) % P
    y3 = (s*(x1-x3) - y1) % P

    return x3, y3

def multiply_point(g_x, g_y, a, b, P, k_pr):
    k_pub_x = g_x
    k_pub_y = g_y

    binary_representation = bin(k_pr)[2:]

    # Iterate through the binary digits, ignoring the MSB
    for bit in binary_representation[1:]:
        k_pub_x, k_pub_y = point_doubling(k_pub_x, k_pub_y, a, b, P)

        if bit == "1":
            k_pub_x, k_pub_y = point_addition(k_pub_x, k_pub_y, g_x, g_y, a, b, P)

    
    return k_pub_x, k_pub_y

def generate_sharedParameter(nBits):
    P = generate_P(128)
    a = generate_a(P)
    b = generate_b(a, P)
    g_x, g_y = generate_G(a, b, P)

    return g_x, g_y, a, b, P


def generate_privateKey(P):
    
     # Generate a random number between 2 and P-1
    k_pr = random.randint(2, P - 1)

    nBits = P.bit_length()
    k_pr = k_pr | (1 << nBits - 1)  # Ensure exactly nBits
    
    return k_pr  

def generate_publicKey(g_x, g_y, a, b, P, k_pr):
    # k_pub = G * k_pr
    return multiply_point(g_x, g_y, a, b, P, k_pr)

def generateSharedKey(g_x, g_y, a, b, P, k_pr):
    # Shared_key, R = k_pr_a * k_pr_b * G mod P
    # R = A*k_pr_b  or B*k_pr_a

    nBits = P.bit_length()

    R_x, R_y = multiply_point(g_x, g_y, a, b, P, k_pr)

    R_x = R_x | (1 << nBits - 1)  # Ensure exactly nBits
    R_y = R_y | (1 << nBits - 1)  # Ensure exactly nBits
    
    return R_x, R_y


def elliptic_curve_for_nBits(nBits):
    g_x, g_y, a, b, P = generate_sharedParameter(nBits)

    num_trails = 7
    total_time_A = 0
    total_time_B = 0
    total_time_R = 0

    for _ in range(num_trails):

        # A
        start_time = time.time() * 1000  

        k_pr_a = generate_privateKey(P)
        k_pub_a = generate_publicKey(g_x, g_y, a, b, P, k_pr_a)

        end_time = time.time() * 1000
        elapsed_time_A = end_time - start_time
        total_time_A += elapsed_time_A

        # B
        start_time = time.time() * 1000

        k_pr_b = generate_privateKey(P)
        k_pub_b = generate_publicKey(g_x, g_y, a, b, P, k_pr_b)

        end_time = time.time() * 1000
        elapsed_time_B = end_time - start_time
        total_time_B += elapsed_time_B

        # third one from here
        start_time = time.time() * 1000

        R_a = generateSharedKey(k_pub_b[0], k_pub_b[1], a, b, P, k_pr_a)
        R_b = generateSharedKey(k_pub_a[0], k_pub_a[1], a, b, P, k_pr_b)

        end_time = time.time() * 1000
        elapsed_time_R = (end_time - start_time) / 2
        total_time_R += elapsed_time_R

    avg_time_A = total_time_A / num_trails
    avg_time_B = total_time_B / num_trails
    avg_time_R = total_time_R / num_trails

    return avg_time_A, avg_time_B, avg_time_R
    

if __name__ == "__main__":
    headers = ["k (bits)", "", "Computation Time For", " "]


    data_headers = [" ", "A", "B", "Shared Key R"]

    #for 128 bits
    time_A_128, time_B_128, time_R_128 = elliptic_curve_for_nBits(128)
    data_128 = [128, time_A_128, time_B_128, time_R_128]

    # 192 bits
    time_A_192, time_B_192, time_R_192 = elliptic_curve_for_nBits(192)
    data_192 = [192, time_A_192, time_B_192, time_R_192]

    # 256 bits
    time_A_256, time_B_256, time_R_256 = elliptic_curve_for_nBits(256)
    data_256 = [256, time_A_256, time_B_256, time_R_256]

    # Create the table and print it
    table = [data_headers, data_128, data_192, data_256]
    print(tabulate(table, headers=headers, tablefmt="grid"))