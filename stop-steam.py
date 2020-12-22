import subprocess
from time import sleep
import time 

def taskkill(task):
    ret = subprocess.run("taskkill /F /IM steam.exe",capture_output=True, startupinfo=si)
    if ret.returncode == 0:
        print ("SUCCESS!!")

def countdown(t): 

    while t: 
        taskkill(t)

        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

# input time in seconds 
t = input("Enter the time in seconds: ") 
# function call 
countdown(int(t)) 

#p=subprocess.run("taskkill /F /IM steam.exe > nul", capture_output=True)
#print(p.stdout)