# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
# https://docs.python.org/2/library/sys.html
# http://www.tutorialspoint.com/python/python_functions.htm
import RPi.GPIO as GPIO
import time,sys


def f(x):
	return {
	'1':18,
	'2':17,
	'3':15,
	'4':14,
}[x]

# sys.argv [1] es la siguiente entrada después del nombre
# Ejemplo : 
# sudo python relay_on.py 1
# si queremos obtener 1, necesitamos sys.argv [1]

pinNum = f(sys.argv[1]) 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinNum,GPIO.OUT)
#turing en el relé actual
GPIO.output(pinNum,0)
#devolver el estado actual del relé
print not GPIO.input(pinNum)

