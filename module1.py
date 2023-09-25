#algorithms project 1
#Justin Stauffer, Nate Bittle, Ellis Benham
#encryption and decryption
#notes for projects
#len function can be used to find the length of a string, ex: count = len(string)
#math.floor rounds down to the nearest integer
#math.sqrt(number) does square root of number
# keys = randint(1,100)
  #  print(keys)
  #the above two lines are how to produce random int if needed
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
def generatepublic(phi):
    z = random.randint(2,phi)
    while math.gcd(z,phi) != 1:
        z = random.randint(2, phi)
    return z
publickey = generatepublic(phi)

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
def encrypt(n, publickey, plaintext):
    ciphertext = []
    for char in plaintext:
        holder = ord(char)
        num = pow(holder, publickey, n)
        ciphertext.append(num)

    return ciphertext
def decrypt(privatekey, n, ciphertext):
    plaintext = ''
    for number in ciphertext:
        holder = pow(number,privatekey,n)
        plaintext += chr(holder)
    return plaintext

    print("RSA keys have been generated.")
def usertype():
    
    print("Please select your user type: ")
    print("\t 1. A public user")
    print("\t 2.The owner of the keys")
    print("\t 3.Exit Program\n")
    number = int(input("Enter your choice: "))
    return number
def publicuser():
    print("As a public user, what would you like to do?")
    print("\t1. Send an encrypted message")
    print("\t2. Authenticate a digital signature")
    print("\t3. Exit")
    userchoice = int(input("Enter your choice: "))
    return userchoice
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
            elif publicnumber == 2:
                print("The following messages are available: ")
                for i in range(0, numberofsignatures):
                     print( (i+1),  ".", signature[i])
                messagechoicesig = int(input("Enter your choice: "))
                #if signature[messagechoicesig -1]
                print("The signature is valid")

            elif publicnumber == 3:
                continue
    if usernumber == 2: #set  ownernumber eqaul to owner function if usernumber is equal to 2 
    #owner options sections
        while ownernumber!=5:
            ownernumber = owner()
            if ownernumber == 1:
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
    





    


        


    
    #ex: if public number == 1, run function that sends an encrypted message or if owner number == 1, run decrypt a recieved message function
    #we can then use the public number and owner number in the same way we used user number with if statemenst and make more functions
    #we could keep using if functions to keep it organized and looking better but it would require more functions, we could just put everything inside of the owner and public user function and not have it jumping around to different functions, ex: if(ownernumber == 3 run show the keys function, or could just do it all inside the owner function)
    #ex: if public number == 1, run function that sends an encrypted message or if owner number == 1, run decrypt a received message function
    #we can then use the public number and owner number in the same way we used user number with if statements and make more functions
    