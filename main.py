from inputs import get_gamepad
from asyncio import run

from bluetooth_telescope import BluetoothTelescope

async def main():
    telescope = BluetoothTelescope(
        'D8:A9:8B:7E:1E:D2',
        '0000ffe1-0000-1000-8000-008805f9b34fb',
        isEquatorial=True,
        lookAt=[[0,0],[0,0]],
        destination=None
    )
    maxInt = 2**15 # signed int16
    debug = False

    while True:
        events = get_gamepad()
        if debug: print(str(events))
        for event in events:
            if debug: print(event.timestamp, event.ev_type, event.code, event.state)

            if event.ev_type == 'Key':
                if debug: print('Key event')
                if event.code == 'BTN_THUMBL':
                    if debug: print('BTN_THUMBL')
                    telescope.emergencyStop(0, event.state / maxInt)
                elif event.code == 'BTN_THUMBR':
                    if debug: print('BTN_THUMBR')
                    telescope.emergencyStop(1, event.state / maxInt)
            elif event.ev_type == 'Absolute':
                if debug: print('Absolute event')
                if event.code == 'ABS_X':
                    if debug: print('ABS_X')
                    telescope.move(0, 0, event.state / maxInt)
                elif event.code == 'ABS_Y':
                    if debug: print('ABS_Y')
                    telescope.move(0, 1, event.state / maxInt)
                elif event.code == 'ABS_RX':
                    if debug: print('ABS_RX')
                    telescope.move(1, 0, event.state / maxInt)
                elif event.code == 'ABS_RY':
                    if debug: print('ABS_RY')
                    telescope.move(1, 1, event.state / maxInt)

if __name__ == "__main__":
    run(main())