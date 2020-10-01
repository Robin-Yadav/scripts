
#!/usr/bin/python
import socket

print("\n\n\n\n")
print("    HH     HH         AA        CCCCCCCCCC     KK     KK           ")
print("    HH     HH       AA  AA      CC             KK   KK             ")
print("    HHHHHHHHH      AAAAAAAA     CC             KK KK               ")
print("    HH     HH     AA      AA    CC             KK   KK             ")
print("    HH     HH    AA        AA   CCCCCCCCCC     KK     KK           ")
print("\n\n\n\n")
print("*********************************************************************")
print("*********************************************************************\n")
print("This scanner is only made for security purposes to scan home networks")
print("This can take some time to scan because it is scanning a whole network\n")
print("AUTHOR:3nc0d3dGuy & legitlearner")
print("*********************************************************************")
print("*********************************************************************\n")
print("\n\n")

network = raw_input("Enter your network range(like 192.168.0): ")
start = input("Enter begining port: ")
end = input("Enter ending port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in range (0,255):
	ip = network
	ip = ip+"."+str(i)

	for j in range (start,end+1):
		if s.connect_ex((ip,j)):
			print("Port "+str(j)+" for "+ip+" is closed")
		else:
			print("Port "+str(j)+" for "+ip+" is closed")
