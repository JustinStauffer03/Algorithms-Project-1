#algorithms project 1
#Justin Stauffer, Nate Bittle, Ellis Benham
#encryption and decryption

from ast import Continue
from random import randint
import math
from cmath import e
import random 
import math
import sys
from turtle import goto
#variable declarations
x = False
length = []
plaintext = []
ciphertextstore = []
finaltextstore = []
signature = []
numberoftexts = 0
numberofsignatures = 0
ownernumber = 0
publicnumber = 0
#function definitions

#Randomnumbers is a function that gets two random prime numbers to use in the calculation of p and q
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

#Stores a random number in p and q
p = randomnumbers(x)
q = randomnumbers(x)

#Calculates phi and n
phi = (p-1) * (q-1)
n = p * q

#Generates public key Algorithm found in lecture slides
def generatepublic(phi):
    z = random.randint(2,phi)
    while math.gcd(z,phi) != 1:
        z = random.randint(2, phi)
    return z

#Stores public key in variable
publickey = generatepublic(phi)

a = n
b = phi

#Defines extended_gcd function to use in generation of private key, algorithm found in lecture slides
def extended_gcd(a, b):
    if b == 0:
        return (1,0,a)
    (x,y,d) = extended_gcd(b, a%b)
    return y, x-a//b*y, d

#Generate private key, algorithm found in lecture slides
def genprivatekey(publickey,phi):
    x = extended_gcd(publickey,phi)
    d = x[0] % phi
    return d

#Store the private key in variable
privatekey = genprivatekey(publickey,phi)

#Encrypts the message using the public key
def encrypt(n, publickey, plaintext):
    ciphertext = []
    for char in plaintext:
        holder = ord(char)
        num = pow(holder, publickey, n)
        ciphertext.append(num)

    return ciphertext

#Decrypt the ciphertext using private key
def decrypt(privatekey, n, ciphertext):
    plaintext = ''
    for number in ciphertext:
        holder = pow(number,privatekey,n)
        plaintext += chr(holder)
    return plaintext

    print("RSA keys have been generated.")

    #Interface where user selcts their user type
def usertype():
    
    print("Please select your user type: ")
    print("\t 1. A public user")
    print("\t 2.The owner of the keys")
    print("\t 3.Exit Program\n")
    number = int(input("Enter your choice: "))
    return number
#Public user menu that is used to send message or validate a signature
def publicuser():
    print("As a public user, what would you like to do?")
    print("\t1. Send an encrypted message")
    print("\t2. Authenticate a digital signature")
    print("\t3. Exit")
    userchoice = int(input("Enter your choice: "))
    return userchoice

#Owner menu used to decrypt a message, sign a message, show keys, or generate new set of keys
def owner():
    print("As the owner of the keys, what would you like to do?")
    print("\t1. Decrypt a received message")
    print("\t2. Digitally sign a message")
    print("\t3. Show the keys")
    print("\t4. Generating a new set of keys")
    print("\t5. Exit")
    ownerchoice = int(input("Enter your choice: "))
    return ownerchoice
#section for first prompt
usernumber = 0  #usernumber is equal to the first choice from the prompt

#Here begins the loop to move back and forth between menus
while usernumber != 3: 
    publicnumber = 0
    ownernumber = 0
    usernumber = usertype()   

    if usernumber == 1:   #if choice is equal to 1, set publicnumber to the choice of the public user prompt
        while publicnumber != 3:
            publicnumber = publicuser()
        #public user options section
            if publicnumber == 1: 
                plaintext = input("Enter the message to encrypt: ")
                numberoftexts+=1
                length.append(len(plaintext))
                ciphertext = encrypt(n, publickey, plaintext) 
                ciphertextstore.append(ciphertext)
            if publicnumber == 2:
                if numberofsignatures == 0:
                    print("There are no messages available.")
                else:
                    print("The following messages are available: ")
                    for i in range(0, numberofsignatures):
                         print( (i+1),  ".", signature[i])
                    messagechoicesig = int(input("Enter your choice: "))
                    if messagechoicesig > numberofsignatures or messagechoicesig <= 0:
                        print("The signature is invalid.")
                    else:
                        print("The signature is valid.")
            elif publicnumber == 3:
                continue
    if usernumber == 2: #set  ownernumber eqaul to owner function if usernumber is equal to 2 
    #owner options sections
        while ownernumber!=5:
            ownernumber = owner()
            if ownernumber == 1:
                if numberoftexts == 0:
                    print("There are no messages available.")
                else: 
                    print("The following messages are available: ")
                
                
                    for i in range(0, numberoftexts):
                        finaltext = decrypt(privatekey, n, ciphertextstore[i])
                        finaltextstore.append(finaltext)
                        print( (i+1),  ". Length = ", length[i])
                    messagechoice = int(input("Enter your choice: "))
                    print("The decrypted message is : ",  finaltextstore[messagechoice-1])
            if ownernumber == 2:
                 getsignature = input("Enter a message: ")
                 numberofsignatures+=1
                 signature.append(getsignature)
                 print("Message Signed and Sent")
            if ownernumber == 3:
             print ("Public Key: " , n , "," , publickey , ")")
             print ("Private Key: " , privatekey)
            if ownernumber == 4:
                 p = randomnumbers(x)
                 q = randomnumbers(x)
                 phi = (p-1) * (q-1)
                 n = p * q
                 publickey = generatepublic(phi)
                 a = n
                 b = phi
                 privatekey = genprivatekey(publickey,phi)
                 print ("New RSA Keys Have Been Generated")
            if ownernumber == 5:
                continue
    elif usernumber == 3: #exits with code zero if option 3 is chosen
        print("Bye for now!")
        sys.exit(0)
    






    


        


    
