from machine import Pin 
import time 

p5 = P(5,Pin.IN)
p4 = P(4,Pin.OUT,value =0)
button_durum = 0
while True :
    button_durum=p5.value()

    if button_durum == True:
        p4.on()
    else :
        print(button_durum)

