import requests

from requests.structures import CaseInsensitiveDict

import os
try:
	import requests
except:
	os.system("pip install requests")
	import requests
	
import sys

import time
from datetime import datetime
now = datetime.now()
datetime = now.strftime("%d/%m/%Y, %H:%M:%S")


red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

ured = '\e[4;31m'

bhred = '\e[1;91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"


logo=(red+"""
      _____      _                  _____ _    _
     / ____|    | |                / ____| |  | |
    | |    _   _| |__   ___ _ __  | (___ | |__| |
    | |   | | | | '_ \ / _ \ '__|  \___ \|  __  |
    | |___| |_| | |_) |  __/ |     ____) | |  | |
     \_____\__, |_.__/ \___|_|    |_____/|_|  |_|
            __/ |
           |___/                        \33[93m[ V 1.0 ]""")

line=(yellow+"================================================================================================================")
tversion=(green+"\t\t     Version : 1.0.0 ")

devoloper=(green+"\t\tDevoloped By : SH TASRIF ")

tname=(cyan+"\t\t ✯✯SH Email Spoofing✯✯")

def psb(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
        
def header():
	os.system("clear || cls")
	os.system("lolcat logo.txt")
	print(color_off)
	print(tname)
	print(" ")
	print(devoloper)
	print('')
	print(line)
	print(" ")

