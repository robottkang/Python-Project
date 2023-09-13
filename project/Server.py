import socket
import tkinter as tk
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostbyname(socket.getfqdn())
PORT = 23456
BUFFER = 1024
print(HOST)
sock.bind((HOST, PORT))

print('UDP 서버 시작...')

# 데이터 수신
def receive_data():
    while True:
        data, addr = sock.recvfrom(BUFFER)

        received_data = data.decode()
        text_box.insert(tk.END, '수신된 데이터: ' + received_data + ', 보낸 ip: ' + addr[0] + ', 보낸 port: ' + str(addr[1]) +'\n')
        text_box.see(tk.END)

def send_data():
    server_ip = ip_entry.get()
    server_port = int(port_entry.get())
    data = send_entry.get()
        
    sock.sendto(data.encode(), (server_ip, server_port))
    text_box.insert(tk.END, '전송한 데이터: ' + data + '\n')
    text_box.see(tk.END)
    
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
port_entry.insert(0, "5000")

# 데이터 송신을 위한 엔트리 입력창 생성
port_label = tk.Label(window, text='보낼 데이터:')
port_label.pack()

send_entry = tk.Entry(window)
send_entry.pack()

send_button = tk.Button(window, text='전송', command=send_data)
send_button.pack()

# 텍스트 창 생성
text_box = tk.Text(window)
text_box.pack()
def show_message_box(title, message):
    tk.messagebox.showinfo(title, message)

# 스레드 시작
receive_thread = threading.Thread(target=receive_data)
receive_thread.daemon = True
receive_thread.start()

tk.messagebox.showinfo('메시지', '프로그램 시작')


window.mainloop()