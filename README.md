# usb-gamepad
 Use HID gamepad to control telescope motors on Windows/Linux/Darwin
 
# telescope_driver
Use this project on a raspberry pi and install [telescope_driver](https://github.com/DethCount/telescope_driver) on an arduino to send commands to a MKS Base 1.0 board to control telescope motors with your gamepad. \
Use [ptpip-d5300](https://github.com/DethCount/ptpip-d5300) on your raspberry pi to live view your camera while controling the telescope.

# Getting started
> python3 main.py

Wait for bluetooth connection then :
- use gamepad joypad. It sends MOVE commands with normalized speed ([-1;1]) through Bluetooth. X is left-right on left joypad, Y is up-down on right joypad.
- use joypad clicking: It will send STOP command. Not implemented yet.
