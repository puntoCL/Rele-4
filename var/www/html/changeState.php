<?php 
// http://php.net/manual/en/function.exec.php
// si tenemos el valor POST llamado "clicked"
if(isset($_POST['clicked'])){

	if($_POST['clicked']  == 'true' ){
			// ejecutando el comando: sudo python relay_on.py id
			// donde el id es la cantidad de relevo que queremos activar / desactivar
		exec("sudo python /home/pi/relay_on.py " . $_POST['relayId']);
		echo "true";
	}else{
		exec("sudo python /home/pi/relay_off.py " . $_POST['relayId']);
		echo "false";
	}
}
