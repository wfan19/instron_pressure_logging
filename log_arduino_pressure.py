#!/usr/bin/env python3

import serial

with serial.Serial("/dev/ttyACM0", 115200, timeout=5) as arduino:
    try:
        while True:
            b_newline = arduino.readline()
            b_newline = b_newline[0:-2]
            str_newline = b_newline.decode()
            print(str_newline)
    except Exception as e:
        if isinstance(e, KeyboardInterrupt):
            print("Killing program")
        else:
            print(e)