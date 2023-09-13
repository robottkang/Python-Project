# 파일 수신
# UDP_cli.py

import socket
import select

UDP_IP = "192.168.45.130"
IN_PORT = 5005
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))
i = 0
while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("File name:", data)
        data=data.decode()
        #file_name = data.strip() + 'a'
        file_name = '{}.jpg'.format(i)
        i += 1
    f = open(file_name, 'wb')

    while True:
        print('.')
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print("%s Finish!" % file_name)
            f.close()
            break
sock.close()