#This program returns the Gyro and Acceleration values of the sensor.
import time 
import board
import adafruit_mpu6050
import os 

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    time.sleep(0.1)
    os.system('clear')

