# Program Made To Generate Secure Password Phrases
# Notes: To fix the user directory issue just ask the user for their name and then store the input into a variable

import random
from time import sleep
import os
import sys

os.system('cd passgen')

if os.path.exists("/home/nax/passgen") == True:
    os.system('cd passgen')
if os.path.exists("/home/nax/passgen") == False:
    print("Error finding directory.")
    print("Quitting program...")
    sleep(3)
    sys.exit("Please make sure that the passgen folder is inside your Home directory.")

def splash():
    os.system('cat passgensplashscreen.txt')

splash()

sleep(2)

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#&*^!%$~"
pw_length = 0 # set this value to how long you want your password to be; do not set to anything over 71 characters
mypw = ""

while True:
    try:
        pw_length_ask = int(raw_input("How long would you like your password to be? "))
        final_pw_length = pw_length + int(pw_length_ask)
        print("Pass length set to " + str(final_pw_length) + ".")
        break
    except ValueError:
        print("You must enter a number.")

for i in range(final_pw_length):
    next_index = random.randrange(len(alphabet))
    mypw = mypw + alphabet[next_index]

passtype = raw_input("What service are you using? ")
line = "Your password for " + passtype + " is : " + mypw
print line

writeyn = raw_input("Would you like to write your password to a text file? Y/n ")
writeyn = writeyn.strip() # makes sure that no white space is around

if writeyn == 'Y':
    print('Written to passwords.txt')
    f = open("passwords.txt", "a+") # "append"
    f.write(passtype + " - " + mypw)

if writeyn == 'n':
    print('Writting Stopped.')

while writeyn != 'n' and writeyn != 'Y':
    writeyn = raw_input("You must enter Y or n " + "\nWould you like to write your password to a text file? Y/n")
    writeyn = writeyn.strip()
    if writeyn == 'n' or writeyn == 'N' or writeyn == 'no' or writeyn == 'No':
        print 'Writing Stopped.'
        break
    elif writeyn == 'Y' or writeyn == 'y' or writeyn == 'yes' or writeyn == 'Yes':
        print('Written to passwords.txt')
        f = open("passwords.txt", "a+")
        f.write(passtype + " - " + mypw)
        break
