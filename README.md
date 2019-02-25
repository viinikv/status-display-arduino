# status-display-arduino

Shows current time and bitcoin price on a display on my wall

Prepare Arduino Uno:
* Install Arduino IDE
* Install https://github.com/rjbatista/tm1638-library
* Flash serial-to-tm1640.ino

Prepare server:
```
sudo apt install python3-websocket
sudo cp 10-status-display-arduino.rules /etc/udev/rules.d/
```

Run program:
```
bash status-display-arduino.sh
```
