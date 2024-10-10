import pigpio
import time

SERVO_PIN_1 = 18
SERVO_PIN_2 = 27

pi = pigpio.pi()  # 라즈베리 파이의 GPIO 제어

# 서보 모터 각도 설정 함수
def set_servo_angle(servo_pin, angle):
    pulse_width = 500 + (angle / 180.0) * 2000
    pi.set_servo_pulsewidth(servo_pin, pulse_width)

try:
    while True:
        command = input("Enter command (1 or 0): ")

        if command == '1':
            set_servo_angle(SERVO_PIN_1, 100)
            set_servo_angle(SERVO_PIN_2, 0)
            time.sleep(0.4)

            set_servo_angle(SERVO_PIN_1, 0)
            set_servo_angle(SERVO_PIN_2, 100)
            time.sleep(0.5)

            set_servo_angle(SERVO_PIN_1, 100)
            set_servo_angle(SERVO_PIN_2, 0)
            time.sleep(0.4)

        elif command == '0':
            set_servo_angle(SERVO_PIN_1, 100)
            set_servo_angle(SERVO_PIN_2, 0)

except KeyboardInterrupt:
    pass

finally:
    pi.stop()  # pigpio 정지
