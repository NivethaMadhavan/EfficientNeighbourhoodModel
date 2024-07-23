from machine import Pin
import time

led = Pin(16, Pin.OUT)
sensor = Pin(15, Pin.IN)

try:
    while True:
        if sensor.value() == 1:
            led.value(0)  # Turn off LED
        else:
            led.value(1)  # Turn on LED
        time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage
except Exception as e:
    print("An error occurred:", e)
