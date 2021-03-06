#obteniendo la biblioteca principal de GPIO
import RPi.GPIO as GPIO
#obtener la biblioteca de tiempo
import time

# configurando un modo actual
GPIO.setmode(GPIO.BCM)
#eliminando los warings
GPIO.setwarnings(False)
#creando una lista (matriz) con el numero de GPIO que usamos
pins = [18,17,15,14] 

#estableciendo el modo para todos los pines para que todos esten encendidos 
GPIO.setup(pins, GPIO.OUT)

#bucle de pines = 18 sigiendo 17 ,15, 14
for pin in pins :
	#configurando el GPIO en ALTO o 1 o verdadero
	GPIO.output(pin,  GPIO.HIGH)
	#Espera de 0,5 segundos
	time.sleep(0.5)
	#configurar el GPIO en BAJO o 0 o falso
	GPIO.output(pin,  GPIO.LOW)
	#Espera de 0,5 segundos
	time.sleep(0.5)

	#Verificar si el rele actual se esta ejecutando e imprimirlo
	if not GPIO.input(pin) : 
		print("Pin "+str(pin)+" Esta trabajando" )
		

#lo mismo, pero el testeo es hacia atras
#para loop donde pin = 14 next 15,17,18

for pin in reversed(pins) :
	GPIO.output(pin,  GPIO.HIGH)
	time.sleep(0.5)

	GPIO.output(pin,  GPIO.LOW)
	time.sleep(0.5)


#limpieza de todos los GPIO 
GPIO.cleanup()
print "Todos los reles apagados"
