#UDP 클라이언트 프로그램
import socket
send_cnt = 0
BUFFSIZE = 1024
port = 5000
IP_SERVER = '172.30.1.130'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = input("Message to send: ")    
    sock.sendto(msg.encode(),(IP_SERVER, port))
    send_cnt = send_cnt + 1
    if send_cnt > 10 :
        break
    #data = sock.recv(BUFFSIZE)
    #print( data )
