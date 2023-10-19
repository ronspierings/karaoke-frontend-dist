
echo Starting http server on http://localhost:8000
cd /home/admin/Desktop/frontend/karaoke-frontend-dist
lxterminal -e python3 -m http.server &

echo Starting Websockets server on ws://localhost:8765
cd /home/admin/Desktop/scripts/
lxterminal -e python3 ws_server.py &


chromium-browser --start-fullscreen --app=http://localhost:8000/index.html &