import os
import subprocess 
def cmd(string):
    os.system(string)
    if string == "sub":
        print("Subscribe to my Youtube channel :)")
        print("youtube.com/channel/UCZTTYlt__gmGFIi-05BkeWg")
    elif string == "first":
        print("the first youtube video ever")
        print("https://www.youtube.com/watch?v=jNQXAC9IVRw")

host = subprocess.getoutput("hostname")
