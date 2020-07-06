

window=$(xdotool selectwindow)
while read lin; do
xdotool type --delay 60 --window $window "$lin
"
sleep 0.6
if [[ $lin == help* ]] ; then xdotool type --window $window "q"; fi
done <client.py
