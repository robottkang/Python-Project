import socket
BUFSIZE = 1024
port = 5000
address = ("172.19.5.129", port)                        # (주소, 포트 번호) 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)                                     	# 서버 연결 요청
while True:
    msg = input("Your turn. Message to send: ")
    s.send( msg.encode( ) )                           	# 서버에게 메시지 전송 
    data = s.recv(BUFSIZE)                            	# 서버로부터 메세지 수신 
    print("Received message: %s" %data.decode( ) )  
                                                        # byte형을 문자열로 변환

