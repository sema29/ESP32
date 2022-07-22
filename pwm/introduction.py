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



---------------------------

led = PWM(Pin(14), 5000)

while True:
 for dutyCycle in range(0, 1024):
  led.duty(dutyCycle)
  print(dutyCycle)
  sleep(0.2)
