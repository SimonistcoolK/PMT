import os 

def log(string):
    print(string)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
"""
i made this bc I needed a way to clear the sreen without having always to write
os.system("cls" if os.name == "nt" else "clear")
"""