<?php 
// ejecutando el archivo y obteniendo la salida

exec("sudo python /var/www/html/firstCheck.py " ,$output);

// la salida está codificada en json
echo json_encode($output); 
