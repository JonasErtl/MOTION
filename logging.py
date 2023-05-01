import time
import board
import adafruit_mpu6050
import os 
import client

#I2C Setup 
i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    #Compensation for Gyro Bias 
    x = round(mpu.gyro[0] + 0.01986460150976955 ,2)
    y = round(mpu.gyro[1] + 0.49588791280790145 ,2)
    z = round(mpu.gyro[2] + 0.004100478185762012,2)
    gyro_data = (x,y,z)
    print(f"Gyro: X {x}, Y {y}, Z {z}")
    client.send(gyro_data)
    time.sleep(0.1)
    os.system('clear')


