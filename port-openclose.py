#!/usr/bin/python

import socket

ip=raw_input("Enter the ip: ")
start=input("Enter begining port: ")
end=input("Enter ending port: ")

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range(start,end+1):
	if s.connect_ex((ip,i)):
		print "Port", i, "is closed"
	else:
		print "Port", i, "is open"
