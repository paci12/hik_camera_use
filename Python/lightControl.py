import Jetson.GPIO as GPIO
import time
from getstate import GetState

light_pin = 18  # 定义点灯引脚



def light():
    GPIO.setmode(GPIO.BOARD)  # 定义引脚模式
    GPIO.setup(light_pin, GPIO.OUT, initial=GPIO.LOW)  # 点灯控制器，初始化为低电平
    GPIO.setwarnings(False)
    get_state = GetState()
    while True:
        if get_state.wirerope_move_state == 1:
            GPIO.output(light_pin, GPIO.HIGH)
        else:
            GPIO.output(light_pin, GPIO.LOW)




if __name__ == '__main__':
    light()


