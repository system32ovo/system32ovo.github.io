dim a'变量
randomize
a =int(rnd*100)'随机0-100
do
b=inputbox("猜个数字吧")
if int(b)>a then
msgbox"大了"
end if
if int(b)<a then
msgbox"小了"
end if
if int(b)=a then
msgbox"你猜对了"
exit do
end if
loop