#TestKills Port scanner import socket
import socket

ip = socket.gethostbyname(socket.gethostname()) #your IP address

for port in range(65535): #all port are in 0-65535 
	try: 
		serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		serv.bind((ip,port))

	except: 
		print('[OPEN] Port Open :',port)
	serv.close()
