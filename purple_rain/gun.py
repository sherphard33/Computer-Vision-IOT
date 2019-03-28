#Phoenix Aiden Magician Girl
#Code that runs the Gun Turret Servos
from __future__ import division
import time
import Adafruit_PCA9685
import socket
import sys
import RPi.GPIO as GPIO
from thread import *
import datetime
import random
import requests
import os

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)#For gun LED output
GPIO.setup(7, GPIO.IN)#For loop termination button


#------------------------------------========================
pwm = Adafruit_PCA9685.PCA9685()

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60 
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
pwm.set_pwm_freq(60)
#------------------------------------========================

#Set servos to shoot mode
def destroy():
        #time.sleep(2)
        pwm.set_pwm(15, 0, 270)
        time.sleep(1)
        pwm.set_pwm(0, 0, 590)
        time.sleep(1)
#Set servos to rest mode        
def rest():      
        time.sleep(2)       
        pwm.set_pwm(0, 0, 120)
        time.sleep(1)
        pwm.set_pwm(15, 0, 500)
        time.sleep(1)
     
GPIO.cleanup()
            
