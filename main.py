from inputs import get_gamepad

from telescope import Telescope

def main():
    telescope = Telescope(isEquatorial=False, lookAt=[[0,0],[0,0]], destination=None)
    maxInt = 2**15-1 # signed int16

    while True:
        events = get_gamepad()
        print(str(events))
        for event in events:
            print(event.timestamp, event.ev_type, event.code, event.state)

            if event.ev_type == 'Key':
                print('Key event')
                if event.code == 'BTN_THUMBL':
                    print('BTN_THUMBL')
                    telescope.emergencyStop(0, event.state / maxInt)
                elif event.code == 'BTN_THUMBR':
                    print('BTN_THUMBR')
                    telescope.emergencyStop(1, event.state / maxInt)
            elif event.ev_type == 'Absolute':
                print('Absolute event')
                if event.code == 'ABS_X':
                    print('ABS_X')
                    telescope.move(0, 0, event.state / maxInt)
                elif event.code == 'ABS_Y':
                    print('ABS_Y')
                    telescope.move(0, 1, event.state / maxInt)
                elif event.code == 'ABS_RX':
                    print('ABS_RX')
                    telescope.move(1, 0, event.state / maxInt)
                elif event.code == 'ABS_RY':
                    print('ABS_RY')
                    telescope.move(1, 1, event.state / maxInt)

if __name__ == "__main__":
    main()