#UDP 클라이언트 프로그램

import socket
BUFFSIZE = 1024
port = 5000
IP_SERVER = '172.30.1.130'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_cnt = 0

for i in range (0, 3, 1) :
    msg = input("Message to send: ");    
    sock.sendto(msg.encode(),(IP_SERVER, port))

    