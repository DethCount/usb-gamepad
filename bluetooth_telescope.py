from asyncio.exceptions import CancelledError
import time

from asyncio import create_task, get_event_loop
from bleak import BleakClient

from telescope import Telescope

class BluetoothTelescope(Telescope):
    def __init__(self, deviceAddr, characteristicUuid, isEquatorial = False, lookAt = [[0, 0], [0, 0]], destination = None):
        super().__init__(isEquatorial, lookAt, destination)

        self.lastMove = [[None, None], [None, None]]
        self.moveTask = [[None, None], [None, None]]

        self.deviceAddr = deviceAddr
        self.characteristicUuid = characteristicUuid
        self.client = None

    def _requireClient(self):
        if self.client != None:
            if not self.client.is_connected().result():
                raise Exception('Device not connected')
            return

        self.client = BleakClient(self.deviceAddr)

    def _doMove(self, axisIdx, direction, amount):
        self._requireClient()

        print(self.client)

        t = time.time()
        if self.lastMove[axisIdx][direction] == None:
            self.lastMove[axisIdx][direction] = t
            return

        # print(t, self.lastMove[axisIdx][direction], amount)
        dt = t - float(self.lastMove[axisIdx][direction])
        if dt > 0.1:
            self.lastMove[axisIdx][direction] = t
            return

        cmd = None
        if (axisIdx == 0 and direction == 0) or (axisIdx == 1 and direction == 1):
            cmd = 'MOVE ' + ('Y' if axisIdx == 1 else 'X') + ' ' + '{:.16f}'.format(amount)

        if cmd != None:
            print(cmd)
            self.moveTask[axisIdx][direction] = create_task(self.client.write_gatt_char(self.characteristicUuid, bytes(cmd, 'utf-8')))
            self.lastMove[axisIdx][direction] = t