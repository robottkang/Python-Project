#UDP 클라이언트 프로그램

import socket
BUFFSIZE = 1024
port = 5000
IP_SERVER = '172.19.3.237'##서버 ip
sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
udp_cnt = 0

while True:
    data = sock.recv(BUFFSIZE)
    print( data.decode() )
    if data == "hifrom"  :
        print("recv good")