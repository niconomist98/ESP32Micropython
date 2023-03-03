import dht
import machine
from machine import Pin
import time


d = dht.DHT11(Pin(15))
#using deepsleep method
while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print('Temperature: {}°C\tHumidity: {}%'.format(temp, hum))
    machine.deepsleep(10000)