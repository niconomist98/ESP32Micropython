import dht
import machine
from machine import Pin

d = dht.DHT11(Pin(15))
buf_size = 250
temp_buf = bytearray(buf_size)
hum_buf = bytearray(buf_size)
temp_sum = 0
hum_sum = 0
index = 0

# Define a function to compute the moving average of temperature and humidity
def moving_average(buf, value, buf_sum):
    buf_sum -= buf[index]
    buf_sum += value
    buf[index] = value
    index = (index + 1) % buf_size
    return buf_sum / buf_size

# Configure deep sleep mode
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
interval = 1000  # 1s interval
rtc.alarm(rtc.ALARM0, interval)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    temp_sum = moving_average(temp_buf, temp, temp_sum)
    hum_sum = moving_average(hum_buf, hum, hum_sum)
    print('Temperature: {:.2f}°C\tHumidity: {:.2f}%\tMoving Average: {:.2f}°C\t{:.2f}%'.format(temp, hum, temp_sum, hum_sum))
    machine.deepsleep()