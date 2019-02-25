<?php 
$command = escapeshellcmd('python -W ignore D:\Mihir\project\beprojectseptember\spectrogram.py');
$output = shell_exec($command);
echo $output;
?>