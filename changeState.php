<?php 
// http://php.net/manual/en/function.exec.php
// si tenemos el valor de POST llamado "clicked"
if(isset($_POST['clicked'])){

	if($_POST['clicked']  == 'true' ){
		// ejecutando el comando : sudo python relay_on.py id
		// donde el id es la cantidad de relevo que queremos encender / apagar
		exec("sudo python /var/www/html/Rele-4/relay_on.py " . $_POST['relayId']);
		echo "true";
	}else{
		exec("sudo python /var/www/html/Rele-4/relay_off.py " . $_POST['relayId']);
		echo "false";
	}
}
