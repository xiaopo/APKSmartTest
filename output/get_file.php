<?php
header('Access-Control-Allow-Origin: *');
$date = './';
$temp=scandir($date);
$file_arr = array();
foreach($temp as $v){
  $a=$date.'/'.$v;
  //如果是文件夹则执行
  if(is_dir($a) && $v != '.' && $v != '..'){
    $file_arr[] = $v;
  }
}
echo json_encode($file_arr);
exit;