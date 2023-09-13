#UDP 클라이언트 프로그램
import socket
import keyboard
send_cnt = 0
BUFFSIZE = 1024
port = 5000
IP_SERVER = '172.19.5.129'
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = input("Message to send: ")
    if msg == "qqq!!" :
        print("udp close")
        break
    elif msg == "reset!!" :
        print("send_cnt reset")
        msg = None
        send_cnt = 0
    if msg != None :
        sock.sendto(msg.encode(),(IP_SERVER, port))
        send_cnt = send_cnt + 1
    
    if send_cnt > 10  :
        break
    #data = sock.recv(BUFFSIZE)
    #print( data )

sock.close()