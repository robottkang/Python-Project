import cv2
import os
import datetime


cap = cv2.VideoCapture(0)    # 0번 카메라 연결
duration = 10 # 녹화 시간(초)
start_time = datetime.datetime.now()
a = 0
while 1:
    if os.path.exists('./record{}.avi'.format(a)):
        #   
        a += 1 
    else :
        file_path = './record{}.avi'.format(a)# 저장할 파일 경로 이름 ---①        
        break
    
if cap.isOpened:
    fps = 15.0                     # FPS, 초당 프레임 수
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))                        # 프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # VideoWriter 객체 생성
    
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording',frame)
            out.write(frame)# 파일 저장
            if (datetime.datetime.now() - start_time).seconds > duration+4:
               # print("시작시간: ",start_time,"  현재시간: ", datetime.datetime.now() )
                print( (datetime.datetime.now() - start_time).seconds )
                break
            if cv2.waitKey(int(1000/fps)) != -1: 
                break
        else:
            print("no frame!")
            break
    out.release()                                   # 파일 닫기
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()