import dht
import machine

d = dht.DHT11(machine.Pin(15))
d.measure()



temperature = d.temperature()
humidity =  d.humidity()

print(temperature)
print(humidity)


d = dht.DHT22(machine.Pin(15))
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)