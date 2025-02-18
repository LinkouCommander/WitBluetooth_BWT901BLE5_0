## WitBluetooth_BWT901BLE5_0

https://support-73.gitbook.io/witmotion-sdk/ble-5.0-protocol

## 蓝牙5.0传感器示例程序

## 说明文档

https://wit-motion.yuque.com/wumwnr/ltst03/rorzux5fl78bswi3?singleDoc# 《蓝牙5.0协议-姿态传感器》


## Update Overview

This repository primarily focuses on modifications to the Python code. The key changes include:

- Implementing parallel processing for data retrieval and sensor operation.
- Modularizing the startup process embedded within the DeviceModel.
- Simplifying command structures.

## Main Functions

- **`start_imu()`**: Initializes the device and returns an error code.
- **`updateData()`**: Retrieves processed data (default is the angular velocity in three axes, measured in rad/s).
- **`stop_imu()`**: Safely shuts down the device and merges threads.