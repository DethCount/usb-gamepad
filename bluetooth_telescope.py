import time
import functools

from asyncio import create_task
from bleak import BleakClient

from telescope import Telescope

class BluetoothTelescope(Telescope):
    def __init__(self, client, characteristicUuid, isEquatorial = False, lookAt = [[0, 0], [0, 0]], destination = None):
        super().__init__(isEquatorial, lookAt, destination)

        self.client = client
        self.characteristicUuid = characteristicUuid

        self.lastMove = [[None, None], [None, None]]
        self.moveTask = [[None, None], [None, None]]

    async def _doMove(self, axisIdx, direction, amount):
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
            cmd = 'MOVE ' + ('Y' if axisIdx == 1 else 'X') + ' ' + '{:.9f}'.format(amount)

        if cmd != None:
            print(cmd)
            await self.client.write_gatt_char(self.characteristicUuid, bytes(cmd + '\n', 'ascii'), response=True)
            self.lastMove[axisIdx][direction] = t

    async def _doEmergencyStop(self, axisIdx):
        await self.client.write_gatt_char(self.characteristicUuid, b'STOP\n', response=True)
