import socket
import sys

"""Create a socket"""
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
	print "Failed to create a socket. Error code: "+str(msg[0]) + "Error message : "+ msg[1]
	sys.exit()
print 'Socket created!'


"""Connect to a host"""
host = raw_input("Enter hostname: ")
if host == '':
	host = "www.facebook.com"
port = 80

try:
	remote_ip = socket.gethostbyname(host)
	
except socket.gaierror:
	print "Hostname could not be resolved. Exiting!"
	sys.exit()
	
print "IP : "+ remote_ip
s.connect((remote_ip,port))
print "Socket is connected to "+host+" on IP = "+remote_ip

"""Send request to host"""
message = "GET / HTTP/1.1\r\n\r\n"

try:
	s.sendall(message)
except socket.error:
	print "send failed!"
	sys.exit()
	
print "Message sent successfully!"
 
"""Recieve data from host"""

reply = s.recv(10240)
print reply
