import time
z = 0
def heavy_work(name):
    global z
    result = 0
    z += 1
    for i in range(400000):
        result += i
    print('%s done' % name )
    
    
if __name__ == '__main__':
    import threading
    start = time.time()
    threads = []
    for i in range(4):
        t = threading.Thread(target=heavy_work, args=(i, ))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()  # 스레드가 종료될 때까지 대기

    end = time.time()
    print(z)
    print("수행시간: %f 초" % (end - start))