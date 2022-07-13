# Setup ESP32 with Thonny

## Get Thonny

[Thonny](https://thonny.org/)


## Get ESPtool

pip install esptool

## Update Configuration

1) Tools -> Open Thonny Data Folder

2) Open Configuration.ini

3) Close Thonny

4) Add these setting and save and close file.

```
[ESP32]
port = /dev/ttyUSB0
dtr = False
rts = False
```

5) Reopen Thonny
6) From lower right corner go to "Configure Interpreter"
7) Change interpreter to MicroPython (ESP32)
8) Select port as /dev/ttyUSB0
9) In the lower right choose "Install or update firmware"
10) Choose the firmware you downloaded from [here](https://github.com/lemariva/micropython-camera-driver/blob/master/firmware/micropython_camera_feeeb5ea3_esp32_idf4_4.bin)
11) Flash device with new firmware
12) Test Python prompt
