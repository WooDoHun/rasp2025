import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


LED = 11
LED1= 13
LED2= 15


GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

while 1:
	GPIO.output(LED1, GPIO.HIGH)
	GPIO.output(LED2, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(LED1, GPIO.LOW)
	GPIO.output(LED2, GPIO.LOW)
	time.sleep(1)
	GPIO.output(LED1, GPIO.LOW)
	GPIO.output(LED, GPIO.LOW)
	GPIO.output(LED2, GPIO.LOW)
	time.sleep(1)
	GPIO.output(LED, GPIO.HIGH)
	GPIO.output(LED2, GPIO.HIGH)
	time.sleep(1)
	
	GPIO.output(LED, GPIO.LOW)
	GPIO.output(LED2, GPIO.LOW)
	time.sleep(1)
	GPIO.output(LED, GPIO.HIGH)
	GPIO.output(LED1, GPIO.HIGH)
	GPIO.output(LED2, GPIO.HIGH)
	time.sleep(1)

	GPIO.output(LED1, GPIO.LOW)
	GPIO.output(LED, GPIO.LOW)
	GPIO.output(LED2, GPIO.LOW)
	time.sleep(1)
