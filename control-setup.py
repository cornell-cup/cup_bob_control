import RPi.GPIO as GPIO
import time
import serial
import smbus2



#Ground
GND_PIN = 6


### PINS FOR U2D2 POWER HUB FOR THE MOTOR

DATA_TO_DYXL = 8
DATA_FROM_DYXL = 10


### PINS FOR IMUs, multiple IMUs with different I2C addresses can be connected to SDA1
SDA_PIN = 3
SCL_PIN = 5
IMU_PWR = 4  #5V


#No pins needed for cameras


######################### GPIO Setup #####################

#GPIO mode
GPIO.setmode(GPIO.BCM)


#UART communication for U2D2 POWER HUB
UART_PORT = "/dev/serial0"  #default port for UART
BAUD_RATE = 57600  #default frequency of communication
ser = serial.Serial(UART_PORT, BAUD_RATE, timeout = 1)

#Initialize I2C for IMUs
bus = smbus2.SMBus(1) #I2C primary bus


#IMU CONNECTING FUNCTION
