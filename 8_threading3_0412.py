import threading
def f_timer():
    print("1번 스레드 타이머 함수가 실행됩니다.")
    t = threading.Timer(1.0, f_timer)
    t.start()
def s_timer():
    print("2번 스레드 타이머 함수가 실행됩니다.")
    t1 = threading.Timer(1.0, s_timer)
    t1.start()

t = threading.Timer(1.0, f_timer)
t.start()
t1 = threading.Timer(1.0, s_timer)
t1.start()
print("main")