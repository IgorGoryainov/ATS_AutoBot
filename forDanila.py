from engines import *
import socket
import argparse
import time
import os
def setup_gpio():
    os.system("sudo pigpiod")  # Launching GPIO library
    time.sleep(1)  # As i said it is too impatient and so if this delay is removed you will get an error
    import pigpio
    ESC = 17
    STEER = 18
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(ESC, 0)
    pi.set_servo_pulsewidth(STEER, 0)
    time.sleep(1)
    # pi.set_servo_pulsewidth(ESC, 1500)
    # time.sleep(1)

    return pi,ESC,STEER
pi, ESC, STEER = setup_gpio()
control(pi, ESC, 1500, STEER, 75)
time.sleep(3)
control(pi, ESC, 1600, STEER, 75)
time.sleep(3)
control(pi, ESC, 1390, STEER, 95)
time.sleep(3)

#control(pi, ESC, 1390, STEER, 75) серва прямо, движки назад
#control(pi, ESC, 1390, STEER, 55) поворот вправа сервой

