<?php 
// ejecutando el archivo y obteniendo la salida 
// http://php.net/manual/en/function.exec.php

exec("sudo python /var/www/html/Rele-4/firstCheck.py " ,$output);

// la salida está codificada en json
echo json_encode($output); 
