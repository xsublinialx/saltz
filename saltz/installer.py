# saltz installer

import os
import sys
import getpass
from time import sleep
from termcolor import colored, import cprint

get_login = getpass.getuser()
get_dir = os.getcwd()
greenY = colored("Y")
redN = colored("n ")

areColor = colored("Are you sure you would like to run the installer? ", "red")
finalAreColor = areColor + greenY + "/" + redN 
askInstall = raw_input(finalAreColor)

if askInstall == "Y" or "y":
	print("Starting install...")
	sleep(2)
	os.chdir("~" + get_login)
	os.system("unzip saltz-1.0.2-alpha.zip")
if askInstall.upper == "n" or "N":
	print("Stopping Install...")
	
