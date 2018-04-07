# Program Made To Generate Secure Password Phrases

import random
from time import sleep
import os
import sys
import getpass

os.system('clear')

get_login = getpass.getuser()
get_dir = os.getcwd()

if os.path.exists("/home/' + get_login + '/saltz/saltz/splash") == True:
    os.chdir('/home/' + get_login + '/saltz/saltz/splash')
if os.path.exists("/home/' + get_login + '/saltz/saltz/splash") == False:
    sleep(1)
    print("Error finding directory.")
    sleep(3)
    print("Quitting program...")
    sleep(3)
    sys.exit("Please make sure that the saltz folder is inside your Home directory.")

ransplash = random.choice(os.listdir("/home/' + get_login + '/saltz/saltz/splash"))

if ransplash == 'splash1':
    os.system('cat splash1')

if ransplash == 'splash2':
    os.system('cat splash2')

if ransplash == 'splash3':
    os.system('cat splash3')

sleep(2)

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#&*^!%$~"
pw_length = 0
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
writeyn = writeyn.strip()

if writeyn == 'Y':
    print('Written to passwords.txt')
    f = open("passwords.txt", "a+") # "append"
    f.write("\n" + passtype + " - " + mypw)

if writeyn == 'n':
    print('Writting Stopped.')

while writeyn != 'n' and writeyn != 'Y':
    writeyn = raw_input("You must enter Y or n " + "\nWould you like to write your password to a text file? Y/n ")
    writeyn = writeyn.strip()
    if writeyn == 'n' or writeyn == 'N' or writeyn == 'no' or writeyn == 'No':
        print 'Writing Stopped.'
        break
    elif writeyn == 'Y' or writeyn == 'y' or writeyn == 'yes' or writeyn == 'Yes':
        print('Written to passwords.txt')
        f = open("passwords.txt", "a+")
        f.write(passtype + " - " + mypw)
        break
