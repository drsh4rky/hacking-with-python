import signal
import time


def _keyboard_interrupt_handler(signal, frame):
    print("Keyboard interrupt handler")
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    return None


signal.signal(signal.SIGINT, _keyboard_interrupt_handler)

time.sleep(10)

print("Reset")

time.sleep(10)
