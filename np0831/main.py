import os
import cv2
import threading
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# SQLite DB 생성 및 연결
conn = sqlite3.connect('photos.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS photos (id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT)''')
conn.commit()

# 카메라 쓰레드 플래그
camera_thread_flag = False

# 카메라 스레드 함수
def camera_thread():
    global camera_thread_flag
    cap = cv2.VideoCapture(0)  # 카메라 번호 0번
    while camera_thread_flag:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')

# 버튼을 눌렀을 때 실행되는 라우트
@app.route('/capture', methods=['POST'])
def capture():
    if request.method == 'POST':
        ret, frame = cv2.VideoCapture(0).read()  # 카메라 촬영
        if ret:
            photo_path = 'static/photo.jpg'
            cv2.imwrite(photo_path, frame)  # 사진 저장
            cursor.execute('INSERT INTO photos (path) VALUES (?)', (photo_path,))
            conn.commit()
            return 'Captured and saved!'
        else:
            return 'Failed to capture photo.'

if __name__ == '__main__':
    #camera_thread_flag = True
    #camera_thread_obj = threading.Thread(target=camera_thread)
    #camera_thread_obj.start()

    app.run(host='0.0.0.0', port=5000, debug=False)

