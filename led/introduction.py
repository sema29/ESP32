from machine import Pin 
import time

p2=Pin(2) # ledin pin atamasını yaptık

while True: # devre güç aldıkça çalışması için sonsuz döngüde
    led.on()
    time.sleep(1)   # led yandıktan sonra 1 saniye sleep
    led.off()
    time.sleep(1)   # led söndükten sonra 1 saniye sleep









