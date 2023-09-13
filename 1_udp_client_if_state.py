#UDP 클라이언트 프로그램

import socket
BUFFSIZE = 1024
port = 5000
IP_SERVER = '172.16.2.135'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_cnt = 0

while True:
    msg = input("Message to send: ");    
    sock.sendto(msg.encode(),(IP_SERVER, port))
    udp_cnt = udp_cnt + 1
    if udp_cnt == 1 :
        sock.sendto("1".encode(),(IP_SERVER, port))
    elif udp_cnt == 2 :
        sock.sendto("2".encode(),(IP_SERVER, port))
    elif udp_cnt == 3 :
        sock.sendto("3".encode(),(IP_SERVER, port))
    else :
        udp_cnt = 0
        break
