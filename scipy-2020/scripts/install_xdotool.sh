xdotool type --window $(xdotool selectwindow) "pip install yaqd-core yaqd-system-monitor yaqd-control yaqc
"


xdotool type --window $(xdotool selectwindow) "yaqd edit-config system-monitor
"


xdotool type --window $(xdotool selectwindow) "i[scipy]
port=38202
"

xdotool key --window $(xdotool selectwindow) Escape

xdotool type --window $(xdotool selectwindow) ":wq
"

xdotool type --window $(xdotool selectwindow) "yaqd-system-monitor
"
