dim a'����
randomize
a =int(rnd*100)'���0-100
do
b=inputbox("�¸����ְ�")
if int(b)>a then
msgbox"����"
end if
if int(b)<a then
msgbox"С��"
end if
if int(b)=a then
msgbox"��¶���"
exit do
end if
loop