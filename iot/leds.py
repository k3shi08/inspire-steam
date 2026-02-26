# Name : Abigail Wangechi
# Date : 26/2/2026
# Program to blink leds


from machine import Pin

red_led = Pin(28, Pin.OUT) 
yellow_led = Pin(27,Pin.OUT)
while True:
    red_led.on()
    yellow_led.off()
    import time
    time.sleep(1) # Wait for USB to become ready
    red_led.off()
    yellow_led.on()
    time.sleep(1) 
    print("Learning IoT")
