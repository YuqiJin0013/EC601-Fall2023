'''
620031587
Net-Centric Computing Assignment
Part A - RSA Encryption
'''

import random


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
# def multiplicative_inverse(e, phi):
#     d = 0
#     x1 = 0
#     x2 = 1
#     y1 = 1
#     temp_phi = phi
    
#     while e > 0:
#         temp1 = temp_phi/e
#         temp2 = temp_phi - temp1 * e
#         temp_phi = e
#         e = temp2
        
#         x = x2- temp1* x1
#         y = d - temp1 * y1
        
#         x2 = x1
#         x1 = x
#         d = y1
#         y1 = y
    
#     if temp_phi == 1:
#         return d + phi
''' extended Euclidean algorithm to find the multiplicative inverse of two numbers'''
def eea(a,b):
    if b==0:return (1,0)
    (q,r) = (a//b,a%b)
    (s,t) = eea(b,r)
    return (t, s-(q*t) )

'''wraps the result of eea and ensures the inverse is a positive number'''
def multiplicative_inverse(x,y):
    inv = eea(x,y)[0]
    if inv < 1: inv += y #we only want positive values
    return inv
'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

'''This function generates an RSA key pair given two prime numbers, p and q. 
It ensures that p and q are prime and not equal.
It calculates the modulus (n = p * q) and the totient (φ = (p-1) * (q-1)).
It selects a public exponent (e) that is coprime with φ.
It uses the extended Euclidean algorithm to calculate the private exponent (d) to form the public key (e, n) 
and private key (d, n) pairs'''
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q
    #Phi is the totient of n
    phi = (p-1) * (q-1)
    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

'''This function takes a public key (e, n) and plaintext as input.
It converts each character in the plaintext to its ASCII value 
and encrypts it using the formula (char^e) % n. The result is an array of encrypted values'''
def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher
'''This function takes a private key (d, n) and ciphertext as input.
It decrypts each character in the ciphertext using the formula (char^d) % n 
and converts the result back to characters. The result is the decrypted message'''
def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertex and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print ("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print ("Your public key is ", public ," and your private key is ", private)
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print ("Your encrypted message is: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("Decrypting message with private key ", private ," . . .")
    print ("Your message is:")
    print (decrypt(private, encrypted_msg))