import socket
import multiprocessing

def handle_client(conn):
    """클라이언트 연결을 처리하는 함수"""
    conn.send("hello world".encode())
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print("[서버] 받은 메시지:", message)
            conn.send(data)
        except ConnectionResetError:
            print("[서버] 클라이언트가 접속을 해제하였습니다.")
            break
    conn.close()


if __name__ == '__main__':
    # 서버 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 5000))
    server_socket.listen(5)
    print("[서버] 서버가 시작되었습니다.")

    while True:
        # 클라이언트 연결 대기
        conn, addr = server_socket.accept()
        print("[서버] 새로운 클라이언트가 연결되었습니다.", addr)

        # 클라이언트 연결을 처리하는 프로세스 생성
        p = multiprocessing.Process(target=handle_client, args=(conn,))
        p.start()