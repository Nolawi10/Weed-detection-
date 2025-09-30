from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import threading
import time

app = Flask(__name__)

class RoboticArm:
    def __init__(self):
        self.pins = {
            'base': 17,
            'shoulder': 18,
            'elbow': 22,
            'wrist': 23,
            'gripper': 24
        }
        self.setup_gpio()
        self.servos = {}
        self.initialize_servos()
        self.home_position()
    
    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins.values():
            GPIO.setup(pin, GPIO.OUT)
    
    def initialize_servos(self):
        for name, pin in self.pins.items():
            self.servos[name] = GPIO.PWM(pin, 50)
            self.servos[name].start(0)
    
    def move_servo(self, servo_name, angle):
        if servo_name not in self.servos:
            return False
        duty = 2 + (angle / 18)
        self.servos[servo_name].ChangeDutyCycle(duty)
        time.sleep(0.5)
        return True
    
    def home_position(self):
        for name in self.servos:
            self.move_servo(name, 90)
    
    def pick_weed(self, x, y, frame_width, frame_height):
        try:
            base_angle = int((x / frame_width) * 180)
            reach_distance = 1.0 - (y / frame_height)
            
            self.move_servo('base', base_angle)
            self.move_servo('shoulder', int(30 + (60 * reach_distance)))
            self.move_servo('elbow', int(90 - (30 * reach_distance)))
            self.move_servo('wrist', 45)
            self.move_servo('gripper', 0)
            time.sleep(1)
            self.home_position()
            return True
        except Exception as e:
            print(f"Error in pick_weed: {e}")
            return False

# Global arm controller
arm = RoboticArm()

@app.route('/move_arm', methods=['POST'])
def move_arm():
    try:
        data = request.json
        x = data.get('x', 0)
        y = data.get('y', 0)
        width = data.get('width', 640)
        height = data.get('height', 480)
        
        success = arm.pick_weed(x, y, width, height)
        return jsonify({"status": "success" if success else "error"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        for servo in arm.servos.values():
            servo.stop()
        GPIO.cleanup()
