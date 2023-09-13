from flask import Flask, render_template
import sqlite3
import random
import threading
import time

app = Flask(__name__)

# SQLite 데이터베이스 연결
db_connection = sqlite3.connect('database.db', check_same_thread=False)
db_cursor = db_connection.cursor()

# 데이터베이스 초기화 - 테이블이 없다면 생성
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS random_numbers (
        id INTEGER PRIMARY KEY,
        value INTEGER
    )
''')
db_connection.commit()

# 데이터베이스에 난수 저장을 위한 함수
def save_random_number():
    while True:
        random_value = random.randint(1, 1000)
        db_cursor.execute('INSERT INTO random_numbers (value) VALUES (?)', (random_value,))
        db_connection.commit()
        time.sleep(1)

# 백그라운드에서 난수 저장 함수 실행
random_number_thread = threading.Thread(target=save_random_number)
random_number_thread.daemon = True
random_number_thread.start()

@app.route('/')
def index():
    # 데이터베이스에서 가장 최근에 저장된 값 가져오기
    db_cursor.execute('SELECT value FROM random_numbers ORDER BY id DESC LIMIT 1')
    last_random_number = db_cursor.fetchone()

    return render_template('index.html', last_random_number=last_random_number[0] if last_random_number else None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)