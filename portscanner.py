import socket
import subprocess
import sys
from datetime import datetime

#for blank the screen
subprocess.call('clear' , shell=True)

#input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Banner
print ("#" * 20)
print ("Please wait, scanning remote host", remoteServerIP)
print ("#" * 20)

#date and time of the scan started
tim1 = datetime.now()

#Looking for open ports and doing error handling
try:
    for port in range(1,5000):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print ("port {}:	Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print ("You pressed Ctrl+c")
    sys.exit()

except socket.gaierror:
    print ("Host could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to sever")
    sys.exit()

#check time again
tim2 = datetime.now()

#total time
total = tim2 - tim1

#printing complete msg with total time
print ("scanning Complete in:" , total)