<?php
$npy=$_POST['npy'];
$com = escapeshellcmd("python D:\Mihir\prog\\xampp\htdocs\project\\test.py ".$npy);
$op = shell_exec($com);
echo $op;
?>