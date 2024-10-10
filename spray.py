import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정 (라즈베리 파이의 핀 번호에 맞게)
SERVO_PIN_1 = 18  # 첫 번째 서보 모터 핀 (라즈베리 파이의 GPIO 18 -> 12번 핀)
SERVO_PIN_2 = 27  # 두 번째 서보 모터 핀 (라즈베리 파이의 GPIO 27 -> 13번 핀)

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN_1, GPIO.OUT)
GPIO.setup(SERVO_PIN_2, GPIO.OUT)

# PWM 설정 (주파수 50Hz)
pwm1 = GPIO.PWM(SERVO_PIN_1, 50)
pwm2 = GPIO.PWM(SERVO_PIN_2, 50)

# PWM 시작 (각도를 제어하기 위해 0의 듀티사이클로 시작)
pwm1.start(0)
pwm2.start(0)

def set_servo_angle(servo, angle):
    # 서보 모터의 각도를 설정하는 함수
    duty = 2 + (angle / 18)  # 듀티 사이클을 각도에 맞게 계산 (0~180도 대응)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)  # 각도가 변할 시간을 주기 위해 약간의 딜레이
    servo.ChangeDutyCycle(0)  # 서보 모터가 멈추도록 0으로 설정

try:
    while True:
        command = input("Enter command (1 or 0): ")  # 시리얼 입력 대신 키보드 입력으로 변경

        if command == '1':
            set_servo_angle(pwm1, 100)  # 첫 번째 모터를 100도 회전
            set_servo_angle(pwm2, 0)    # 두 번째 모터는 0도
            time.sleep(0.4)             # 0.4초 대기

            set_servo_angle(pwm1, 0)    # 첫 번째 모터를 다시 0도로 회전
            set_servo_angle(pwm2, 100)  # 두 번째 모터는 100도로 회전
            time.sleep(0.5)             # 0.5초 대기

            set_servo_angle(pwm1, 100)  # 첫 번째 모터를 다시 100도 회전
            set_servo_angle(pwm2, 0)    # 두 번째 모터는 다시 0도로
            time.sleep(0.4)             # 0.4초 대기

        elif command == '0':
            set_servo_angle(pwm1, 100)  # 첫 번째 모터를 100도 유지
            set_servo_angle(pwm2, 0)    # 두 번째 모터는 0도 유지

except KeyboardInterrupt:
    pass

finally:
    pwm1.stop()  # PWM 정지
    pwm2.stop()  # PWM 정지
    GPIO.cleanup()  # GPIO 설정 해제
