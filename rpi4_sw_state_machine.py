import threading
# 필요한 라이브러리를 불러옵니다.
import RPi.GPIO as GPIO 
import time
print("btn evt test\n")

light_on = False

def t_call():
    timer= threading.Timer(0.02, t_call)
    timer.start()
    button_detect(15)
    

def button_detect(channel):
    global btn_cnt, btn_state, light_on
    
    if GPIO.input(button_pin) == GPIO.HIGH and btn_state ==0 :
        btn_state = 1
        
    elif GPIO.input(button_pin) == GPIO.HIGH and btn_state == 1 :
        btn_state = 2
        GPIO.output(led_pin,light_on)
        light_on = not light_on 
        print("btn pushed!")
    
    elif  GPIO.input(button_pin) == GPIO.LOW :
        btn_state = 0
    
btn_cnt = 0
btn_state = 0
led_pin = 18
# 사용할 GPIO핀의 번호를 선정합니다.
button_pin = 15
 # 불필요한 warning 제거
GPIO.setwarnings(False) 
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM) 
# 버튼 핀의 IN/OUT 설정 , PULL DOWN 설정 
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
# Event 방식으로 핀의 Rising 신호를 감지하면 button_callback 함수를 실행합니다.


# LED 핀의 OUT설정
GPIO.setup(led_pin, GPIO.OUT)


t_call()

while 1:
    print("main loop")