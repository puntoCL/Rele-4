# https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
# https://docs.python.org/2/library/sys.html
# https://docs.python.org/2/library/json.html



#obtener la biblioteca principal de GPIO
import RPi.GPIO as GPIO
#time and json
import time
import json

# establecer una lista de pines usados 
pins = [18,17,15,14]

# configurando el modo GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# crear lista vacia
arr = []
# para el bucle de 0 a 3
for x in range(0,4) : 
	#poner todos los reles en estado si GPIO no esta configurado
	GPIO.setup(pins[x],GPIO.OUT)
	#putting the relay state in the empty list 
	arr.append(not GPIO.input(pins[x]))

# imprimiendo la lista de estados en formato json
print json.dumps({0:arr[0],1:arr[1],2:arr[2],3:arr[3]})
