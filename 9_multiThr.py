import time

z = 0
def heavy_work(name):
    global z
    z +=1
    result = 0
    for i in range(4000000):
        result += i
    print('%s done, ' % name, "변수 공유 불가: ", z)


if __name__ == '__main__':
    import multiprocessing
    cpu_count = multiprocessing.cpu_count()
    print("CPU 코어 개수:", cpu_count)
    
    start = time.time()
    procs = []
    for i in range(20):
        p = multiprocessing.Process(target=heavy_work, args=(i, ))
        p.start()
        procs.append(p)
        print(p)
    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 대기

    end = time.time()
    print("변수 공유 불가: ", z)
    print("수행시간: %f 초" % (end - start))