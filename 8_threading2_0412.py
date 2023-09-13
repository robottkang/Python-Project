import threading
import time
# 스레드에서 실행될 함수
def worker():
    result = 0
    print("스레드 작업 시작")
    for i in range(40000000):
        result += i
    print("쓰레드 작업 끝")

# 스레드 생성 및 실행
t = threading.Thread(target=worker)
t.start()
# 메인 스레드에서 실행될 작업
print("")
print("메인 스레드 작업 시작")
time.sleep(1)
print("메인 스레드 작업 종료")
# 스레드 종료 대기
t.join()
print("프로그램 종료")