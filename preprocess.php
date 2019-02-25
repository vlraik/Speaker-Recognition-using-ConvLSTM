<?php 
$audio=str_replace(' ','',basename($_FILES["audio"]["name"]));
$target_dir = "D:/Mihir/prog/xampp/htdocs/project/Audiofiles/";
$target_file = $target_dir . $audio ;

#echo $audio;

if(move_uploaded_file($_FILES["audio"]["tmp_name"], $target_file))
{
$pyfile = "python D:\Mihir\prog\\xampp\htdocs\project\convert_file.py ".$audio ;
$command = escapeshellcmd($pyfile);
$output = shell_exec($command);
$com = escapeshellcmd("python D:\Mihir\prog\\xampp\htdocs\project\spectrogramnew.py ".$output);
$op = shell_exec($com);
}
echo $output;
?>