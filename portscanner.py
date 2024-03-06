import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear' , shell=True)


remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)


print ("#" * 20)
print ("Please wait, scanning remote host", remoteServerIP)
print ("#" * 20)


tim1 = datetime.now()

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


tim2 = datetime.now()


total = tim2 - tim1


print ("scanning Complete in:" , total)
