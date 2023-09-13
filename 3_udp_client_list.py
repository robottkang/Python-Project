#UDP 클라이언트 프로그램

import socket
BUFFSIZE = 1024
port = 5000
IP_SERVER = '192.168.45.235'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = input("Message to send: ");    
sock.sendto(str(len(msg)).encode(),(IP_SERVER, port)) # 프로토콜 
sock.sendto(msg.encode(),(IP_SERVER, port))			  # 프로토콜
print(str(len(msg)))

sock.sendto(msg[0:2].encode(),(IP_SERVER, port))
print(msg[0:2])    