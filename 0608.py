import socket
import tkinter as tk
import threading
from tkinter import messagebox
# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 호스트와 포트 번호 설정
HOST = ''  # 로컬 호스트
PORT = 23456  # 임의의 포트 번호
print(HOST)
# 소켓을 주소와 바인딩
sock.bind((HOST, PORT))

print('UDP 서버 시작...')

def receive_data():
    while True:
        # 데이터 수신
        data, addr = sock.recvfrom(1024)  # 버퍼 크기는 1024 바이트로 설정할 수 있습니다.

        # 수신한 데이터 텍스트 창에 표시
        received_data = data.decode()
        text_box.insert(tk.END, '수신된 데이터: ' + received_data + ', 보낸 ip: ' + addr[0] + ', 보낸 port: ' + str(addr[1]) +'\n')
        text_box.see(tk.END)  # 텍스트 창 스크롤 조정
        
        if received_data == 'eme':
            tk.messagebox.showinfo('메시지', '아무거나 활성화')
def send_data():
    # 입력한 IP와 포트 번호 가져오기
    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    # 서버에 데이터 전송
    data = send_entry.get()
    if data == '920701' :
        show_message_box("경고창", "개인정보유출")
        
    sock.sendto(data.encode(), (server_ip, server_port))
    # 전송한 데이터 텍스트 창에 표시
    text_box.insert(tk.END, '전송한 데이터: ' + data + '\n')
    text_box.see(tk.END)  # 텍스트 창 스크롤 조정
    
# GUI 창 생성
window = tk.Tk()
window.title('UDP 서버 채팅 GUI')

# IP 입력창 생성
ip_label = tk.Label(window, text='보낼 IP:')
ip_label.pack()

ip_entry = tk.Entry(window)
ip_entry.pack()

# 포트 번호 입력창 생성
port_label = tk.Label(window, text='포트 번호:')
port_label.pack()

port_entry = tk.Entry(window)
port_entry.pack()
port_entry.insert(0, "5000")#엔트리 입력창에 기본 포트번호 생
# 데이터 송신을 위한 엔트리 입력창 생성
port_label = tk.Label(window, text='보낼 데이터:')
port_label.pack()

send_entry = tk.Entry(window)
send_entry.pack()

# 전송 버튼 생성
send_button = tk.Button(window, text='전송', command=send_data)
send_button.pack()

# 텍스트 창 생성
text_box = tk.Text(window)
text_box.pack()
def show_message_box(title, message):
    tk.messagebox.showinfo(title, message)

# 데이터 수신을 위한 스레드 시작
receive_thread = threading.Thread(target=receive_data)
receive_thread.daemon = True  # 메인 스레드 종료시 함께 종료되도록 설정
receive_thread.start()

tk.messagebox.showinfo('메시지', '프로그램시작')


window.mainloop()