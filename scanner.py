#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments")
	print("Syntax, Python3 Scanner.py<ip>")
	sys.exit()

print("-" * 50)
print("Scanning Target : " + target)
print("Time Started : "+ str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,1025):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		print("Checking port {}".format(port))
		result = s.connect_ex((target,port)) #if error -> returns int
		if result == 0:
			print("Port is Open {}".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\n Exiting Program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to server!")
	sys.exit()

		
