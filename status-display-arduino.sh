python3 status-display-arduino.py | while true; do tee --output-error=exit /dev/status-display-arduino; sleep 2; done
