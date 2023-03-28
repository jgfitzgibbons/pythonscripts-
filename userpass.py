#This program is a username and password generator
#user has the option to choose what characters go into the password
#the username and password are then written in a textfile of the user's choice
#inputs: user first and last name, password length and choice of character types
#and the file that the user wants their log in information to be written to
#output:username and random password
#Run the program by importing userpass.py

import random, string

def user():

    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")

    uname = first[0] + last[:8]

    return uname

def generatePassword():
    
    length = int(input("How many characters do you want in your password? "))

    while True:
        passwordtype = int(input('1 - Text \n2 - Numbers only\n3 - text and numbers \n4 - text/numbers/special char\nPlease select a number: '))

        if passwordtype ==1:
            pw=''.join(random.choice(string.ascii_letters) for _ in range(length))
            break
        elif passwordtype ==2:
            pw=''.join(random.choice(string.digits) for _ in range(length))
            break
        elif passwordtype ==3:
            pw=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
            break
        elif passwordtype ==4:
            pw=''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(length))
            break
        else:
            print('Please enter a number between 1 and 4\n')
    return pw

def textfile():
    uname = user()
    pw = generatePassword()
    fileName= input("What file should your login information go in? ")
    outfile = open(fileName, "w")
    print(uname, file=outfile)
    print(pw, file=outfile)
    outfile.close()

    print("Login Info has been written to", fileName)

textfile()




    
 

