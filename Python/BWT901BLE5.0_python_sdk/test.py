import asyncio
import bleak
from device_model import BLEIMUHandler
import threading
import time

# test
if __name__ == "__main__":
    handler = BLEIMUHandler()
    debug_code = handler.start_imu()
    if debug_code < 0:
        exit()
    
    try:
        while True:
            time.sleep(1)  # grab data every sec
            rX, rY, rZ = handler.updateData()
            print(f"IMU Data: AsX={rX}, AsY={rY}, AsZ={rZ}")
    except KeyboardInterrupt:
        print("Interrupt")

    handler.stop_imu()