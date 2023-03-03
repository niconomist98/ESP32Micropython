import dht
import machine
import time
import _thread

# Define pin for DHT sensor
dht_pin = 15

# Define pin for user button
button_pin = 0

# Define global variable to keep track of whether or not to print measurements
print_measurements = True

# Define function for Thread1 that prints temperature and humidity measurements
def print_measurements_thread():
    global print_measurements
    # Initialize DHT sensor
    d = dht.DHT11(machine.Pin(dht_pin))
    while True:
        if print_measurements:
            # Measure temperature and humidity
            d.measure()
            temp_c = d.temperature()
            hum = d.humidity()
            # Print measurements
            print("Temperature: {}C, Humidity: {}%".format(temp_c, hum))
            time.sleep(1)

# Define function for Thread2 that reads user button and controls Thread1
def control_measurements_thread():
    global print_measurements
    # Initialize button as input with internal pull-up resistor
    button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)
    while True:
        # Check if button is pressed
        if not button.value():
            # Toggle print_measurements variable
            print_measurements = not print_measurements
            # Wait for button to be released
            while not button.value():
                time.sleep_ms(50)
        time.sleep_ms(50)

# Start Thread1 and Thread2
_thread.start_new_thread(print_measurements_thread, ())
_thread.start_new_thread(control_measurements_thread, ())
