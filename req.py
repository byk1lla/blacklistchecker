from os import system, chdir, mkdir, rmdir, path,getlogin
from time import sleep as w8
from tkinter import messagebox as ms

import re



class renk:
            BLACK = "\033[90m"
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            RED = '\033[31m'
            PURPLE = '\033[95m'
            YELLOW = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            BGRED = '\033[41m'
            BGREEN = '\033[42m'
            BGYELLOW = '\033[43m'
            BGBLUE = '\033[44m'
            BGPURPLE = '\033[45m'
            WHITE = '\033[37m'
            ALERT = '\033[5m'
class err:
        criticerr = renk.ALERT+renk.BGRED+"\n[ ! ] "+renk.RED
        eror = renk.RED+"\n[ X ] "
        warn = renk.YELLOW+"\n[ - ] "
        succ = renk.GREEN+"\n[ + ]  "
        info = renk.BLUE+"\n[ i ] "
def error(msg):
    print(err.criticerr+f"An error occurred!\nError Message is--->{msg}"+renk.ENDC)
    exit(err.info+f"Closing..."+renk.ENDC)




