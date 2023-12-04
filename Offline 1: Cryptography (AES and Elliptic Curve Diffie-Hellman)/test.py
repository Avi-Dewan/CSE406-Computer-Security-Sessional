from Crypto.Random import random
from Crypto.Util import number


def trunchBit(nBits):
    return (1 << nBits) - 1


print(bin(trunchBit(4)))