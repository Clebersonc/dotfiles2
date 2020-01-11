#!/bin/bash
pkill -f "dzen2 -p -title-name status_bar"
# length=1366
height=10
font="NotoSans Nerd Font-11"

xpos=0
ypos=0
# width=140
height=25

# parameters="  -x $xpos -y $ypos -w $width -h $height"
# parameters="  -x $xpos -y $ypos -h $height"
# parameters+=" -fn $font"
# parameters+=" -ta c -bg gray15 -fg gray70"
# parameters+=" -title-name dzentop"

# load() {
#     mem=$(free -m|awk 'NR==2 {print $3}')
#     cpu=$(bc <<< $(ps -eo pcpu |grep -vE '^\s*(0.0|%CPU)' |sed -n '1h;$!H;$g;s/\n/ +/gp'))
# 	echo -ne "^p(_RIGHT)^p(-360)^fg($blue)  ^fg($fg)$mem^fg($yellow)    $icpu ^fg($fg)$cpu"
# }

music() {
    songa=$(mpc current -f "%artist%")
    songb=$(mpc current -f "%title%")
	if [ "${#songa}" -eq 0 ] && echo "$songb" grep '-' &>/dev/null; then
		songa=$(echo "$songb" | cut -d'-' -f1)
		songb=$(echo "$songb" | cut -d'-' -f2)
	fi
	icon=
    if [[ -z $songb ]]; then
        songb=$(mpc current -f "%file%"|cut -d "/" -f2|sed 's/.mp3$//')
    fi
    if [[ -z $(mpc current)  ]]; then
        songa=""; songb=""; icon=""
    fi
	[ ${#songa} -gt 20 ] && songa=$(echo "$songa" | cut -c 1-20)...
	[ ${#songb} -gt 20 ] && songb=$(echo "$songb" | cut -c 1-20)...
	echo -ne "^p(_LEFT)^p(65)^fg(steelblue)$icon  ^fg(gray55)$songa ^fg(gray70)$songb"
}

pomo() {
	status=$(~/.local/bin/pomo status | cut -d' ' -f1)
	session=$(~/.local/bin/pomo status | cut -d' ' -f2 | tr -d '[]-')
	if [ $status == "C" ]; then
		echo -ne "^p(_LEFT)^fg(green)  ^fg(gray50)$session"
	elif [ $status == "B" ]; then
		echo -ne "^p(_LEFT)^fg(skyblue)  ^fg(skyblue)$session"
	elif [ $status == "P" ]; then
		echo -ne "^p(_LEFT)^fg(purple)  ^fg(purple)$session"
	elif [ $status == "R" ]; then
		echo -ne "^p(_LEFT)^fg(deeppink)  ^fg(gray70)$session"
	else
		echo -ne "^p(_LEFT)^fg(steelblue)  ^fg(gray50)$session"
	fi
}
logo() {
	echo -ne "^p(_LEFT)^fg(steelblue)  ^fg(gray40)arch^fg(steelblue)linux ^bg(gray15)"
}

window() {
	title=$(xprop -id "$(xprop -root 32x '\t$0' _NET_ACTIVE_WINDOW | cut -f 2)" _NET_WM_NAME 2>/dev/null | cut -d= -f2 | tr -d '"')
	if [ ${#title} -gt 20 ]; then
		title=$(echo "$title" | cut -c 1-20)...
	fi
	echo -ne "^p(_CENTER)^p(-100)^fg(steelblue)  ^fg(gray70)$title"
}

pingms() {
	ms=$(ping -q -c 1 1.1.1.1 | grep rtt | cut -d= -f2 | cut -d. -f1)
	# ip=$(ip r | awk 'NR==2 {print $9}')
	if [ -z "$ms" ]; then
		ms="  ?"
	fi
	echo -ne "^p(_RIGHT)^p(-465)^fg(steelblue)  ^fg(gray70)$ms"
}
update() {
	packages=$(trizen -Qu | wc -l)
	echo -ne "^p(_RIGHT)^p(-395)^fg(steelblue)   ^fg(gray70)$packages"
}

load() {
	value=$( cut -d' ' -f1 /proc/loadavg)
	avg=$(bc <<< 100-"$value"*100/4)
	total="^fg(steelblue) 鈴 "
	[ "$avg" -lt '0' ] && total="^fg(deeppink)  "
	echo -ne "^p(_RIGHT)^p(-335)$total ^fg(gray70)${avg//-/}%"
}

volume() {
	sound=$(amixer get Master | grep Left | cut -d' ' -f7 | tr -d '[]')
	vol=$(amixer get Master | grep -E -o "[0-9]+%" | tr -d '%' | sed '1q;d')
    if [ "$sound" = "off" ]; then
		bar=$(echo "$vol" | gdbar  -h 7 -w 40 -s o -bg deeppink -fg deeppink -nonl)
        echo -ne "^p(_RIGHT)^p(-255)^fg(steelblue) 墳  $bar"
    else
		bar=$(echo "$vol" | gdbar  -h 7 -w 40 -s o -fg gray70 -nonl)
		echo -ne "^p(_RIGHT)^p(-255)^fg(steelblue) 墳  $bar"
    fi
}

clock() {
    timea=$(date +'%l:%M %p')
    timeb=$(date +'%a %_d')
	echo "^p(_RIGHT)^p(-163)^ca(1,sysinfo.sh)^fg(steelblue) ^fg(gray50)$timea ^fg(gray70)$timeb^ca()"
}


while true; do
	# logo
	pingms
	update
    volume
	window
    music
    load
    clock
	pomo
    sleep 1
done | dzen2 \
	-x "$xpos" -y "$ypos" -h "$height" \
	-fn "$font" -ta c -bg gray15 \
	-fg gray70 -title-name dzentop
