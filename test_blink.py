import unittest
from gpiozero import LED, Device
from gpiozero.pins.mock import MockFactory

# Tell gpiozero to use "Mock" pins instead of real hardware
Device.pin_factory = MockFactory()

class TestLED(unittest.TestCase):
    def test_led_initialization(self):
        # Try to initialize the LED on pin 17
        try:
            led = LED(17)
            # Check if the pin is correctly assigned
            self.assertEqual(led.pin.number, 17)
            print("Test Passed: LED initialized correctly.")
        except Exception as e:
            self.fail(f"LED initialization failed: {e}")

if __name__ == '__main__':
    unittest.main()
