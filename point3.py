import dht
from machine import Pin
import time

d = dht.DHT11(Pin(15))

# Using sleep method
#while True:
#    d.measure()
#    temp = d.temperature()
#    hum = d.humidity()
#    print('Temperature: {}°C\tHumidity: {}%'.format(temp, hum))
#    time.sleep(1)

#Using sleep_ms method
while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print('Temperature: {}°C\tHumidity: {}%'.format(temp, hum))
    time.sleep_ms(1000)