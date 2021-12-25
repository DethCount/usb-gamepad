# usb-gamepad
 Use HID gamepad to control telescope motors on Windows/Linux/Darwin

> python3 main.py

Wait for bluetooth connection then :
- use gamepad joypad. It sends MOVE commands with normalized speed ([-1;1]) through Bluetooth. X is left-right on left joypad, Y is up-down on right joypad.
- use joypad clicking: It will send STOP command. Not implemented yet.
