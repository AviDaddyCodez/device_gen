import os
os.system("pip install requests")
os.system("pip install pyfiglet")
os.system("pip install colored")
clear = lambda: os.system('cls')
clear()
import requests
import threading
import pyfiglet
from colored import attr, back, bg, fg, fore, style
xd="┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄"
f = pyfiglet.figlet_format("    dev_gen", font="slant")
MB = fore.MAGENTA_3A + back.BLACK + style.BLINK
OB = fore.ORANGE_1 + back.BLACK + style.BLINK
BO = fore.BLACK + back.ORANGE_1 + style.BLINK
OM = fore.ORANGE_1 + back.MAGENTA_3A + style.BLINK
WB = fore.BLACK + back.WHITE + style.BLINK
print((fore.ORANGE_1 + back.BLACK + style.BLINK + xd), attr('reset'))
print (MB + f)
print((OB + xd), attr('reset'))
print (OM + "  github.com/forevercynical               discord > cynical#7777", attr('reset'))
x = int(input('Enter Amount of Threads: '))

def device_gen():
    while True:
        deviceId = requests.get("https://forevercynical.o5hej45uqb.repl.co").text
        print(BO + f"\n{deviceId}", attr('reset'))
        with open("deviceIds.txt", "a") as file:
            file.write(f"{deviceId}\n")
        print(MB + "\nSaved to deviceIds.txt")
for i in (list(range(1,x+1))):
    threading.Thread(target = device_gen).start()
