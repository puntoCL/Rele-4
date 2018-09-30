<?php 
// executing file and getting the output 
// ejecutando el archivo y obteniendo la salida

exec("sudo python /home/pi/firstCheck.py " ,$output);

// la salida está codificada en json
echo json_encode($output); 
