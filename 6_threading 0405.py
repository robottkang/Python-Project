import threading
import time

def event_func():
    print("이벤트 함수 실행됨")

def generate_event():
    threading.Timer(1, generate_event).start()
    event_func()

if __name__ == "__main__":
    generate_event()
    while 1:
        print("main")