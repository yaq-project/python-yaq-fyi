window=$(xdotool selectwindow)

xdotool type --delay 30 --window $(xdotool selectwindow) "yaqd enable system-monitor
"
xdotool windowfocus $window

sleep 8

xdotool type --delay 30 --window $(xdotool selectwindow) "yaqd start system-monitor
"
xdotool windowfocus $window

sleep 8

xdotool type --delay 30 --window $(xdotool selectwindow) "yaqd status
"

