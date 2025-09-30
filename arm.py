import RPi.GPIO as GPIO
import time

# Servo pin mapping
BASE_PIN = 17
ARM1_PIN = 27
ARM3_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(BASE_PIN, GPIO.OUT)
GPIO.setup(ARM1_PIN, GPIO.OUT)
GPIO.setup(ARM3_PIN, GPIO.OUT)

# Setup PWM (50Hz for servos)
base = GPIO.PWM(BASE_PIN, 50)
arm1 = GPIO.PWM(ARM1_PIN, 50)
arm3 = GPIO.PWM(ARM3_PIN, 50)

# Start with neutral position (7.5% duty ~ 90 degrees)
base.start(7.5)
arm1.start(7.5)
arm3.start(7.5)

def set_angle(pwm, angle):
    # Angle 0-180 → Duty cycle 2.5 - 12.5
    duty = 2.5 + (angle/18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)

try:
    # Move base left
    set_angle(base, 45)
    time.sleep(1)

    # Raise first arm
    set_angle(arm1, 120)
    time.sleep(1)

    # Lower third arm
    set_angle(arm3, 60)
    time.sleep(1)

    # Move third arm up
    set_angle(arm3, 120)
    time.sleep(1)

    # Turn base right
    set_angle(base, 135)
    time.sleep(1)

finally:
    base.stop()
    arm1.stop()
    arm3.stop()
    GPIO.cleanup()

