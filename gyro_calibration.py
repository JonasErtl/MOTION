import board 
import adafruit_mpu6050
import os 

def progress_bar(total, current):
    bar_length = 20
    progress = current / total
    completed = int(bar_length * progress)
    remaining = bar_length - completed
    bar = '#' * completed + ' ' * remaining
    print(f'[{bar}] {int(progress * 100)}%' ,end='\r')

def bias_calculation(lis):
    total = 0
    for value in lis:
        total = total + value
    avg = total/len(lis)
    print(avg)



X_Values = []
Y_Values = []
Z_Values = []

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)
print("Calibration in Progress...")
for i in range(3020): 
    X_Values.append(mpu.gyro[0])
    Y_Values.append(mpu.gyro[1])
    Z_Values.append(mpu.gyro[2])
    progress_bar(3020, i+1)

os.system("clear")
print("Calculating X Bias...")
bias_calculation(X_Values)
print("Calculating Y Bias...")
bias_calculation(Y_Values)
print("Calculating Z Bias...")
bias_calculation(Z_Values)
