import upip
import _thread
import time
import dht
from machine import Pin

# Thread1 function that reads temperature and humidity measurements
def thread1_func():
    dht_sensor = dht.DHT22(Pin(15))
    while True:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print("Temperature: {:.2f}°C, Humidity: {:.2f}%".format(temperature, humidity))
        time.sleep(1)

# Thread2 function that controls Thread1's behavior based on user button status
def thread2_func():
    button = Pin(0, Pin.IN)
    # set up a flag to indicate whether the button is pressed or not
    button_pressed = False
    while True:
        # read button status
        if button.value() == 0:  # button is pressed (active low)
            if not button_pressed:
                button_pressed = True
                # stop Thread1 from printing
                print("Button pressed, stopping Thread1...")
                event.set()
        else:  # button is released
            if button_pressed:
                button_pressed = False
                # resume Thread1 printing
                print("Button released, resuming Thread1...")
                event.clear()
        time.sleep(0.1)

# create an event to signal Thread1 to stop printing
event = thread.Event()

# create Thread1 and Thread2 objects
thread1 = thread.Thread(target=thread1_func)
thread2 = thread.Thread(target=thread2_func)

# start both threads
thread1.start()
thread2.start()

# wait for both threads to finish
thread1.join()
thread2.join()
