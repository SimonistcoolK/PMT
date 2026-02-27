#!/usr/bin/env python3
import requests, time

webhook_url = "your_webhook_url_here"

class col():
    # The "col" class is for colors!
    GREEN = "\033[32m"
    END = "\033[0m"
    BOLD = "\033[1m" 

class main():
    # The "main" class is for allmost anything :)
    def bann():
        # The "bann" function is for printing the "PMT" Ascii banner! 
        print(f"{col.GREEN}██████╗ ███╗   ███╗████████╗")
        print("██╔══██╗████╗ ████║╚══██╔══╝")
        print("██████╔╝██╔████╔██║   ██║   ")
        print("██╔═══╝ ██║╚██╔╝██║   ██║   ")
        print("██║     ██║ ╚═╝ ██║   ██║   ")
        print("╚═╝     ╚═╝     ╚═╝   ╚═╝    \n")
        print("welcome to PMT ")                         
    def op():
        print(f"{col.BOLD}Options :{col.END}")
        print(f"{col.GREEN}")
        print("")


main.bann()
main.op()