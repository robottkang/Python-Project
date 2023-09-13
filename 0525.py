from flask import Flask, Response
import cv2
import numpy as np
import socket
import time
import sys


# 감도 설정(카메라 품질에 따라 조정 필요)
thresh = 25    # 달라진 픽셀 값 기준치 설정
max_diff = 5   # 달라진 픽셀 갯수 기준치 설정
cnt = 0
str_cnt = 0
# 카메라 캡션 장치 준비
a, b, c = None, None, None

i = 0
j = 0
app = Flask(__name__)
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1440)      # 프레임 폭을 480으로 설정 
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)     # 프레임 높이를 320으로 설정

def generate_frames():
    global i
    while True:
        success, frame = camera.read()
        if camera.isOpened():
            ret, a = camera.read()         # a 프레임 읽기
            ret, b = camera.read()         # b 프레임 읽기
            '''''''''''''''''''''''''''''''''''''''''''''''''''''
            1번주석
            ret, buffer = cv2.imencode('.jpg', frame_pic)
            frame_p = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_p + b'\r\n')   

            '''''''''''''''''''''''''''''''''''''''''''''''''''''       
            while ret:
                ret, c = camera.read()     # c 프레임 읽기
                draw = c.copy()         # 출력 영상에 사용할 복제본
                 
                if not ret:
                    break
                
                # 3개의 영상을 그레이 스케일로 변경
                a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
                b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
                c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

                # a-b, b-c 절대 값 차 구하기 
                diff1 = cv2.absdiff(a_gray, b_gray)
                diff2 = cv2.absdiff(b_gray, c_gray)

                # 스레시홀드로 기준치 이내의 차이는 무시
                ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
                ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

                # 두 차이에 대해서 AND 연산, 두 영상의 차이가 모두 발견된 경우
                diff = cv2.bitwise_and(diff1_t, diff2_t)

                # 열림 연산으로 노이즈 제거 ---①
                k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
                diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)
            ##================================================================
                # 차이가 발생한 픽셀이 갯수 판단 후 사각형 그리기
                diff_cnt = cv2.countNonZero(diff)
                
                if diff_cnt > max_diff:
                    nzero = np.nonzero(diff)  # 0이 아닌 픽셀의 좌표 얻기(y[...], x[...])
                    cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])), \
                                        (max(nzero[1]), max(nzero[0])), (0,255,0), 2)
                    cv2.putText(draw, "Motion Detected", (10,30), \
                                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,255))
                    print(diff_cnt)   
                   
                    if diff_cnt > 10000 :
                        print(diff_cnt)                       
                        ret_pic, frame_pic = camera.read()
                        '''''''''''''''''''''''''''''''''''''''''''''''''''''
                        2번주석
                        ret, buffer = cv2.imencode('.jpg', frame_pic)
                        frame_p = buffer.tobytes()
                        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_p + b'\r\n')   
                        '''''''''''''''''''''''''''''''''''''''''''''''''''''
                        frame_pic = cv2.flip(frame_pic,1)
                        cv2.imwrite('mytest{}.jpg'.format(i),frame_pic)
                        
                        net_filename = 'mytest{}.jpg'.format(i).encode()
                        #print("Sending {} ...".format(file_name))
                        f = open('mytest{}.jpg'.format(i), "rb")
                        i += 1  
                        f.close()
                     
            ##================================================================            
                # 컬러 스케일 영상과 스레시홀드 영상을 통합해서 출력
                #stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
                #cv2.imshow('motion sensor',stacked )

                # 다음 비교를 위해 영상 순서 정리
                a = b
                b = c
                
                if cv2.waitKey(1) & 0xFF == 27:
                    break             
               
                
             
                #if not success:
                #    break
                #else:

            '''''''''''''''''''''''''''''''''''''''''''''''''''''
            3번주석
            ret, buffer = cv2.imencode('.jpg', frame_pic)
            frame_p = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_p + b'\r\n')   

            '''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/')
def index():
    return (
        "<h1>'testPage_0524'</h1>"
        "<img src='/video_feed'>"
    )

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    '''''''''''''''''''''''''''''''''''''''''''''''''''''
    4번주석
    ret, buffer = cv2.imencode('.jpg', frame_pic)
    frame_p = buffer.tobytes()
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_p + b'\r\n')   

    '''''''''''''''''''''''''''''''''''''''''''''''''''''


