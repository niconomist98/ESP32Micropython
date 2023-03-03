import dht
import machine
import time
import ustruct
import array

# Define the buffer size
BUFFER_SIZE = 250

# Define the RTC RAM memory address
RTC_RAM_START_ADDR = 0x60000000

# Define the struct format for the buffer
BUFFER_FORMAT = "<" + "hh" * BUFFER_SIZE

# Define the deep sleep time in seconds
DEEP_SLEEP_TIME = 10

# Initialize the DHT11 sensor
d = dht.DHT11(machine.Pin(15))

# Create the buffer in RTC RAM area
buf = bytearray(BUFFER_SIZE * 2)
buffer = array.array('h', buf)

# Define the index for the circular buffer
buffer_index = 0

# Define the variables for moving average
temperature_sum = 0
humidity_sum = 0

# Check if the device woke from deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    # Read the buffer from RTC memory
    buf = machine.RTC().memory()
    # Unpack the buffer into the array
    buffer = array.array('h', ustruct.unpack_from(BUFFER_FORMAT, buf))

while True:
    # Measure the temperature and humidity
    d.measure()
    temperatura = d.temperature()
    humedad = d.humidity()

    # Update the circular buffer
    buffer[buffer_index * 2] = temperatura
    buffer[buffer_index * 2 + 1] = humedad

    # Update the moving average variables
    temperature_sum += temperatura
    humidity_sum += humedad

    # Increment the buffer index
    buffer_index = (buffer_index + 1) % BUFFER_SIZE

    # Compute the moving averages
    temperature_avg = temperature_sum / BUFFER_SIZE
    humidity_avg = humidity_sum / BUFFER_SIZE

    # Print the values
    print("Temperatura:", temperatura, "Moving average:", temperature_avg)
    print("Humedad:", humedad, "Moving average:", humidity_avg)

    # Reset the moving average variables
    temperature_sum -= buffer[(buffer_index - 1) * 2]
    humidity_sum -= buffer[(buffer_index - 1) * 2 + 1]

    # Write the buffer to RTC memory
    buf = ustruct.pack(BUFFER_FORMAT, *buffer)
    machine.RTC().memory(buf)

    # Put the device into deep sleep mode
    machine.deepsleep(DEEP_SLEEP_TIME * 1000)
