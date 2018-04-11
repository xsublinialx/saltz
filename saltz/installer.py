# saltz installer

import os 
from time import sleep
from termcolor import colored, import cprint

greenY = colored("Y")
redN = colored("n ")

areColor = colored("Are you sure you would like to run the installer? ", "red")
finalAreColor = areColor + greenY + "/" + redN 
askInstall = raw_input(finalAreColor)

if askInstall == "Y" or "y":
	print("Starting install...")
	sleep(2)
if askInstall.upper == "n" or "N":
	print("Stopping Install...")
	
