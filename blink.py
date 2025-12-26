from gpiozero import LED
from signal import pause
from time import sleep

# Define the LED on GPIO pin 17
led = LED(17)

print("Blinking LED on GPIO 17... Press Ctrl+C to stop.")

try:
    while True:
        led.on()       # Turn the LED on
        sleep(1)       # Wait for 1 second
        led.off()      # Turn the LED off
        sleep(1)       # Wait for 1 second
except KeyboardInterrupt:
    # This handles the Ctrl+C exit cleanly
    print("\nStopping the blinker.")
