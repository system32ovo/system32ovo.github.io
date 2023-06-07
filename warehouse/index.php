<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>system32ovo的小仓库</title>
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<style>
body {
  background-image: url("bg.jpg"); /* 设置背景图片 */
  background-color: #f1f1f1; /* 设置背景颜色 */
  background-size: cover; /* 铺满整个屏幕 */
  background-position: top center; /* 置于页面顶部居中位置 */
}
</style>
</head>
<body>
<h1 align="center" class="rainbow">system32ovo的小仓库         Tips: 下面的utility-tools是实用工具文件夹哦</h1>
<a href="http://system32ovo123.best6.top"><返回主页</a>

<style>
.rainbow {
    background: -webkit-linear-gradient(45deg, #f90000,#ff8c00,#ffe500,#90ee02,#3cb371,#00ced1,#4300ff,#8b00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>

<?php
function getFiles($dir){
    $files = array();
    $dir_list = scandir($dir);
    foreach($dir_list as $file){
        if($file !== '.' && $file !== '..'){
            $filePath = $dir.'/'.$file;
            if(is_dir($filePath)){
                // 如果当前文件夹名是 update 则跳过
                if ($file === 'update') {
                    continue;
                }
                $files = array_merge($files, getFiles($filePath));
            }else{
                $files[] = $filePath;
            }
        }
    }
    return $files;
}

$dir = './';
$file_list = getFiles($dir);

echo "<ul>";
foreach ($file_list as $file) {
    $url = str_replace($_SERVER['DOCUMENT_ROOT'], '', $file);
    $filename = substr($file, 3);
    echo "<li><a href=\"$url\">$filename</a></li>";
}
echo "</ul>";
?>

</body>
</html>
