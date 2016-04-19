import socket
import subprocess
import sys
import os
import urllib
import lxml.html
from ftplib import FTP

from datetime import datetime

## Clear the screen
subprocess.call('clear', shell=True)

## Enter Host to scan
remoteServer = "localhost"
## remoteServer = input("Enter a remote host to scan: ")
## remoteServerIP = remoteServerIP = socket.gethostbyname(remoteServer)
remoteServerIP = "217.31.1.1"
print(remoteServerIP)
remoteServerIP.rsplit('.',1)[0]
## print(remoteServerIP.rsplit('.',1)[0] + '.111')
## This is just a nice touch that prints out information on which host we are about to scan
print("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

## Check what time the scan started
t1 = datetime.now()

## Using the range function to specify ports (here it will scans all ports between 1 and 1024)

## We also put in some error handling for catching errors

try:
    for ipinc in range(4,254):
        for ipinc2 in range(1,254):
            remoteServerIP2 = remoteServerIP.rsplit('.',2)[0] + "." + str(ipinc) + "." + str(ipinc2)

# print(remoteServerIP2)
            responsePing = os.system("ping -c 1 " + remoteServerIP2 + " > /dev/null")
            #and then check the response...
            if responsePing == 0:
                print(remoteServerIP2 + " is online!")
                for port in range(21,22):
                    print(port)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((remoteServerIP2, port))
                    if result == 0:
                        ## if a socket is listening it will print out the port number
                        print(remoteServerIP2 + " Port {}: \t Open".format(port))
                        ftp = FTP(remoteServerIP2)     # connect to host, default port
                        try:
                            if ftp.login():
                                print ('logged in')                     # user anonymous, passwd anonymous@
                                with open(remoteServerIP2 + '.txt', 'a') as file:
                                    file.write(ftp.retrlines('LIST'))           # list directory contents
                                ftp.quit()
                            else:
                                print ('error inside of ftp')
                        except:
                            print('login not possible')
## HTML get links
##                    connection = urllib.urlopen('remoteServerIP2')
##                    dom =  lxml.html.fromstring(connection.read())
##                    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(lin$
##                        if ('index' in link):
##                            print link
                sock.close()
            else:
                print (remoteServerIP2, 'is down!')

## Dont press any buttons or you will screw up the scanning, so i added a keyboard exception
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
## Here is my host execption, incase you typed it wrong. ( i guess mayeb i should have added this up top)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
## finally socket error incase python is having trouble scanning or resolving the port
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

## Checking the time again
t2 = datetime.now()

## Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

## Printing the information to screen
print('Scanning Completed in: ', total)
