<DOCTYPE HTML
<?php

op = $_GET['op'];
shell_exec("/usr/local/bin/gpio -g mode 6 out");  # FAN 1
shell_exec("/usr/local/bin/gpio -g mode 16 out"); #FAN 2
shell_exec("/usr/local/bin/gpio -g mode 5 out");  #FAN 3
shell_exec("/usr/local/bin/gpio -g mode 21 out"); #DOOR
shell_exec("/usr/local/bin/gpio -g mode 23 out"); #LIGHT 1
shell_exec("/usr/local/bin/gpio -g mode 24 out"); #LIGHT 2
shell_exec("/usr/local/bin/gpio -g mode 25 out"); #LIGHT 3
shell_exec("/usr/local/bin/gpio -g mode 27 out"); # APPLLIANCE 1
shell_exec("/usr/local/bin/gpio -g mode 22 out"); #APPLLIANCE 2

switch(op)
{
    case 1:
        shell_exec("/usr/local/bin/gpio - g write 21 1"); #DOOR ON
        break;
    case 2:
        shell_exec("/usr/local/bin/gpio - g write 21 0"); #DOOR OFF
        break;
    case 3:
        shell_exec("/usr/local/bin/gpio - g write 23 1"); #LIGHT 1 ON
        break;
    case 4:
        shell_exec("/usr/local/bin/gpio - g write 23 0");#LIGHT 1 OFF
        break;
    case 5:
        shell_exec("/usr/local/bin/gpio - g write 24 1");#LIGHT 2 ON
        break;
    case 6:
        shell_exec("/usr/local/bin/gpio - g write 24 0");#LIGHT 2 OFF
        break;
    case 7:
        shell_exec("/usr/local/bin/gpio - g write 25 1");#LIGHT 3 ON
        break;
    case 8:
        shell_exec("/usr/local/bin/gpio - g write 25 0");#LIGHT 3 OFF
        break;
    case 9:
        shell_exec("/usr/local/bin/gpio - g write 6 1");#FAN 1 ON
        break;
    case 10:
        shell_exec("/usr/local/bin/gpio - g write 6 0");#FAN 1 OFF
        break;
    case 11:
        shell_exec("/usr/local/bin/gpio - g write 16 1");#FAN 2 ON
        break;
    case 12:
        shell_exec("/usr/local/bin/gpio - g write 16 0");#FAN 2 OFF
        break;
    case 13:
        shell_exec("/usr/local/bin/gpio - g write 5 1");#FAN 3 ON
        break;
    case 14:
        shell_exec("/usr/local/bin/gpio - g write 5 0");#FAN 3 OFF
        break;
    case 15:
        shell_exec("/usr/local/bin/gpio - g write 27 1");#APPLLIANCE 1 ON
        break;
    case 16:
        shell_exec("/usr/local/bin/gpio - g write 27 0");#APPLLIANCE 1 OFF
        break;
    case 17:
        shell_exec("/usr/local/bin/gpio - g write 22 1");#APPLLIANCE 2 ON
        break;
    case 18:
        shell_exec("/usr/local/bin/gpio - g write 22 0");#APPLLIANCE 2 OFF
        break;

}
include("index.html");
?>

