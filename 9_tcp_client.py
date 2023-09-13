import socket

def run_client():
    """클라이언트 실행 함수"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('server ip 입력!!!', 5000))
    print("[클라이언트] 서버에 연결되었습니다.")

    while True:
        message = input("[클라이언트] 보낼 메시지를 입력하세요 (종료하려면 'exit' 입력): ")
        if message == 'exit':
            break
        client_socket.send(message.encode())
        data = client_socket.recv(1024)
        print("[클라이언트] 받은 메시지:", data.decode())

    client_socket.close()

if __name__ == '__main__':
    run_client()