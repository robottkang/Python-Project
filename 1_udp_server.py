# UDP 채팅 서버 프로그램
import socket
port = 5000
maxsize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
print("Waiting for client")
cnt = 0
while True:
    print("<- ", end='')
    data, addr = sock.recvfrom(maxsize)
    print("받은 데이터: ", data)
    print("보낸 클라이언트 주소(ip): ", addr)    
    if data == "asd" :
        print("l")
    cnt +=1
    if cnt == 10:
        break