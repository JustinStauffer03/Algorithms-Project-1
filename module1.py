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
from random import randint
import math
import sys
#variable declarations

#function definitions
def usertype():
    
    print("RSA keys have been generated.")
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
usernumber = usertype()   #usernumber is equal to the first choice from the prompt
if usernumber == 1:   #if choice is equal to 1, set publicnumber to the choice of the public user prompt
    publicnumber = publicuser()
elif usernumber == 2: #set  ownernumber eqaul to owner function if usernumber is equal to 2 
    ownernumber = owner()
elif usernumber == 3: #exits with code zero if option 3 is chosen
    print("Bye for now!")
    sys.exit(0)
else:
    print("Invalid entry")
    #section for second prompt of public user/owner
    #ex: if public number == 1, run function that sends an encrypted message or if owner number == 1, run decrypt a received message function
#we can then use the public number and owner number in the same way we used user number with if statements and make more functions
