

window=$(xdotool selectwindow)
while read lin; do
xdotool type --delay 60 --window $window "$lin
"
sleep 0.4
done <client.py
