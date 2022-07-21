from machine import Pin, ADC 
import time 

adc = ADC (Pin(32))

while True:
    adcValue = adc.read()
    print(adcValue)
    time.sleep(0.5)