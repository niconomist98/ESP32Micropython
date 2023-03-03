import dht
import machine
import time

d = dht.DHT11(machine.Pin(15))

while True:
    d.measure()
    temperatura = d.temperature()
    humedad = d.humidity()

    print("Temperatura:", temperatura)
    print("Humedad:", humedad)

    time.sleep(1)
