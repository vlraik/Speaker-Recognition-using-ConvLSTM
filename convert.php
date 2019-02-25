<?php 
$target_dir = "D:/Mihir/prog/xampp/htdocs/project/Audiofiles/";
$target_file = $target_dir . basename($_FILES["audio"]["name"]);
move_uploaded_file($_FILES["audio"]["tmp_name"], $target_file) ;
$audio=basename( $_FILES["audio"]["name"]);
#echo $audio;
$pyfile = "python D:\Mihir\prog\\xampp\htdocs\project\convert_file.py ".$audio ;
$command = escapeshellcmd($pyfile);
$output = shell_exec($command);
echo $output;
$com = escapeshellcmd("python D:\Mihir\prog\\xampp\htdocs\project\spectrogram.py ".$output);
$op = shell_exec($com);
echo $op;
?>