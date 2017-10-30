
import random

BITS = ('0', '1')
ASCII_BITS = 7

def convert_to_bits(n, pad):
	result = []
	while n>0:
		if n%2==0:
			result = [0] + result
		else:
			result = [1] + result
		n = n/2
	while len(result)<pad:
		result = [0] + result
	return result


def string_to_bits(s):
	result = []
	for c in s:
		result = result + convert_to_bits(ord(c),7)
	return result
	
def generate_key(M):
	K = list(M)
	for _ in range(100):
		random.shuffle(K)
	return K
	
def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])	
	
	
def Encrypt():
	S = raw_input("Enter message!\n")
	M = string_to_bits(S)
	K = generate_key(M)
	C = []
	for i in range(0,len(M)):
		C.insert(i,M[i]^K[i])
		
		
		
		
		
		
def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])
	