## MOTION - Movement Observation and Tracking using IMU On-Hand Navigation -- currently not working

Alternative name: SHACE - System for Hand Acceleration and Coordinate Examination  

The aim of this project is to build a system which can detect Hand-Movement and then further process it. This might include visualizing the motion, using it as some sort of movement input, or even running the Data through a Neural Network to recogize letters and shapes which are drawn. 

Step 1: At first there needs to be a program which is run on a mirco-contoller mounted on a persons Hand. This program will need to capture the IMU Data in real time and send them to another client, ideally over wifi, for further processing.  

# The Gyro Calibration Program
This program determines the bias that the Gyroscope has. It is run by typing `python3 gyro_calibration.py`. It will then proceed to calculate the Biases. Nothing else than having the Gyro plugged in is required. 
