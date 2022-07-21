from machine import Pin, PWM
import time 

pwm0 = PWM(Pin(0))
pwm0.freq(1000)

pwm0.duty(0)
time.sleep(1)

pwm0.duty(256)
time.sleep(1)

pwm0.duty(512)
time.sleep(1)

pwm0.duty(1023)
time.sleep(1)

