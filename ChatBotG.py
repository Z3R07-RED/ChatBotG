#!/usr/bin/env python3
# Name        : ChatBotG
# Author      : Z3R07-RED
# Last Change : Mar 2 2021 [01:36:38]
#
# dependencies
import pyautogui
import sys
import os
import signal
import time

# Define colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'


def sig_handler(sig, frame):
    print(GREEN + "\n\nExiting ...\n" + RESET)
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)


def bannerchatbotg():
    print(RED)
    print("\t ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("\t ┃)(-)(-)(-)(-)(-)(-)(-)(-)(-)(-)┃")
    print("\t ┃-------------------------------┃")
    print("\t ┃)(-)" + CYAN + "(C)(h)(a)(t)(B)(o)(t)(G)" + RED + "(-)┃")
    print("\t ┃-------------------------------┃")
    print("\t ┃)(-)(-)(-)(-)(-)(-)(-)(-)(-)(-)┃")
    print("\t ┗━━━━━━━━━━{Z3R07-RED}━━━━━━━━━━┛")
    print(RESET)


def chatbotg_start():
    global filename
    print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("| Entra en un chat lo antes posible ... |")
    print("| [NOTA]: dentro de Kali Linux.         |")
    print("| * En ALGUNOS chat tienes que presionar|")
    print("|   enter muy rápidamente para enviar   |")
    print("|   los mensajes.                       |")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    time.sleep(1)
    for conn in range(11):
        print("TIME: [" + str(conn), end=" == 10]\r")
        time.sleep(1)

        if(conn == 10):
            print(CYAN + "\n\nPress CTRL+c to stop." + RESET)
            print(GREEN + "ChatBotG up and running ..." + RESET)

    time.sleep(1)
    leerfile = open(filename, 'r')

    for i in leerfile:
        # time.sleep(1)
        pyautogui.typewrite(i)
        pyautogui.press("enter")

    print(GREEN + "done!" + RESET)


filename = None
bannerchatbotg()


print(YELLOW + "FUNCIONA:" + RESET)
print("\n[WHATSAPP ]\t[MESSENGER]\t[  AMINO  ]")
print("[Instagram]\t[Facebook ]\t[Telegram ]")
print("\n[*] Ingrese el nombre del archivo que desea enviar.")
print("\nEXAMPLE:\n\tdefault.txt\n\n")
print("El archivo se enviará por línea.")
filechat = input(GREEN + str("\n[+] Enter the file name: ") + RESET)
time.sleep(1)
filenamed = "[*] File: " + RESET + "chats/" + filechat
filenamem = "[*] File: " + RESET + filechat

if os.path.isfile("chats/" + filechat):
    print(CYAN + filenamed)
    filename = "chats/" + filechat
    chatbotg_start()
elif os.path.isfile(filechat):
    print(CYAN + filenamem)
    filename = filechat
    chatbotg_start()
else:
    print(RED + filenamed)
    print(RED + "[!] ERROR: ¡El archivo no existe!" + RESET)
