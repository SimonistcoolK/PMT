#!/usr/bin/env python3
import requests
import time
import col
import console
import smd
console.clear()
webhook_url = "your_webhook_url_here"



class main():
    # The "main" class is for almost anything :)
    def bann():
        # The "bann" function is for printing the "PMT" Ascii banner! 
        print(col.GREEN)
        print("██████╗ ███╗   ███╗████████╗")
        print("██╔══██╗████╗ ████║╚══██╔══╝")
        print("██████╔╝██╔████╔██║   ██║   ")
        print("██╔═══╝ ██║╚██╔╝██║   ██║   ")
        print("██║     ██║ ╚═╝ ██║   ██║   ")
        print("╚═╝     ╚═╝     ╚═╝   ╚═╝    \n")
        print("welcome to PMT ")                         
    def op():
        print(f"{col.BOLD}Options :{col.END}")
        print(f"{col.GREEN}")
        print("1. About") 
    
    def main():
        main.bann()
        main.op()
        ch = input(f"\nAdmin@{smd.host} :~$ ")
        if ch == "1":
            console.clear()
            print(f"{col.BOLD}PMT is a simple tool to send messages to a discord webhook.{col.END}")
            print(f"{col.GREEN}Created by VigilanBytes aka. SimonK{col.END}")
main.main()