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
releases = "\nsaltz-1.0.1-alpha"

areColor = colored("Are you sure you would like to run the installer? ", "red")
finalAreColor = areColor + greenY + "/" + redN 
askInstall = raw_input(finalAreColor)

if askInstall == "Y" or "y":
	print("Starting install...")
	newRelease = raw_input("Would you like to install a new release or use a downloaded release? D: Download N: New Release ")
	if newRelease == "D" or "d":
		print(releases)
	
	sleep(2)
	os.chdir("~" + get_login)
	os.system("unzip saltz-1.0.2-alpha.zip")
if askInstall.upper == "n" or "N":
	print("Stopping Install...")
	
