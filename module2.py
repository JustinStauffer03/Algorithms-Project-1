
from cmath import e
import random 
import math

x = False

def randomnumbers(x):
    

   while x == False:
    x = True
    e=random.randint(3,10000)
    if e < 2:
        x = False
    for i in range (2, int(e**0.5) + 1):
        if e % i == 0:
            x = False
    if x == True:
        return e



p = randomnumbers(x)
q = randomnumbers(x)

phi = (p-1) * (q-1)
n = p * q

print (p)
print (q)
print (phi) 

def generatepublic(phi):
    z = random.randint(2,phi)
    while math.gcd(z,phi) != 1:
        z = random.randint(2, phi)
    return z

publickey = generatepublic(phi)

print (publickey)



a = n
b = phi

def extended_gcd(a, b):
    if b == 0:
        return (1,0,a)
    (x,y,d) = extended_gcd(b, a%b)
    return y, x-a//b*y, d



def genprivatekey(publickey,phi):
    x = extended_gcd(publickey,phi)
    d = x[0] % phi
    return d



privatekey = genprivatekey(publickey,phi)



print (privatekey)
plaintext = input("enter encrypted message")

def encrypt(n, publickey, plaintext):
    ciphertext = []
    for char in plaintext:
        holder = ord(char)
        num = pow(holder, publickey, n)
        ciphertext.append(num)

    return ciphertext


ciphertext = encrypt(n, publickey, plaintext)


print (ciphertext)

def decrypt(privatekey, n, ciphertext):
    plaintext = ''
    for number in ciphertext:
        holder = pow(number,privatekey,n)
        plaintext += chr(holder)
    return plaintext



finaltext = decrypt(privatekey, n, ciphertext)

print (finaltext)




                



   



