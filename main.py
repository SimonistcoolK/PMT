#!/usr/bin/env python3
import time
import col
import console
import smd
import webhook
console.clear()


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
        print("╚═╝     ╚═╝     ╚═╝   ╚═╝    \n\r\n")  
    def op():
        print(f"{col.BOLD}Options :{col.END}")
        print(f"{col.GREEN}")
        print("[1]. About")
        print("[2]. Suggest Idea")
        print("[3]. Execute Terminal Command")
        print("welcome to PMT ")                       
    
    def main():
        main.bann()
        main.op()
        while True:
            ch = int(input(f"\nAdmin@{smd.host} :~ $ "))
            if ch == 1:
                console.clear()
                print(f"{col.GREEN}Created by VigilanBytes aka. SimonK{col.END}")
                q = input("press Enter to contiue ...")
                console.clear()
                main.bann()
                main.op()
            elif ch == 2:
                console.clear()
                print("don't spam!")
                idea = input("suggest an idea for PMT : ")
                webhook.suggest(idea)
                q = input("press Enter to continue ...")
                console.clear()
                main.bann()
                main.op()
            elif ch == 3:
                console.clear()
                print("type 'sub' to get my youtube channel link")
                print("type 'first' to get the first youtube video ever")
                cmd = input("execute command : ")
                smd.cmd(cmd)
                q = input("press Enter to continue ...")
                console.clear()
                main.bann()
                main.op()
main.main()