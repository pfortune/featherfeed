import machine
import time

def read_distance():
    # Initialize the signal pin (replace 'x' with the actual pin number)
    signal_pin = machine.Pin(20, machine.Pin.OUT)

    # Set the pin to low and give a short delay to settle
    signal_pin.low()
    time.sleep_us(2)

    # Send a 10 microsecond pulse
    signal_pin.high()
    time.sleep_us(10)
    signal_pin.low()

    # Change the pin mode to input for receiving the echo
    signal_pin.init(machine.Pin.IN)

    # Measure the duration of the echo signal
    duration = machine.time_pulse_us(signal_pin, 1, 1000000)
    if duration < 0:
        duration = 0

    # Calculate the distance (340.29 m/s is the speed of sound)
    distance = (duration * 0.0343) / 2

    # Reset the pin to output for the next reading
    signal_pin.init(machine.Pin.OUT)

    return distance
