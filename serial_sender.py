import serial

ser = serial.Serial("/dev/pts/15")
ser.write(bytes([0x54, 0x43, 0x00, 0x01, 0x00, 0x02, 0x00, 0x10, 0x00, 0x04, 0x00, 0x05, 0x00]))

print("finish")