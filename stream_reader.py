import struct

class StreamReader:
    def __init__(self, data):
        super(StreamReader, self).__init__()

        self.data = data
        self.pos = 0

    def _conv(self, vals):
        converted = b''

        for val in vals:
            converted += val.to_bytes(1, byteorder='little')

        return converted


    def readInt8(self):
        pos2 = self.pos + 1
        val = struct.unpack('b', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readUint8(self):
        pos2 = self.pos + 1
        val = struct.unpack('B', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readInt16(self):
        pos2 = self.pos + 2
        val = struct.unpack('h', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readUint16(self):
        pos2 = self.pos + 2
        val = struct.unpack('H', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readInt32(self):
        pos2 = self.pos + 4
        val = struct.unpack('i', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readUint32(self):
        pos2 = self.pos + 4
        val = struct.unpack('I', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readInt64(self):
        pos2 = self.pos + 8
        val = struct.unpack('q', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readUint64(self):
        pos2 = self.pos + 8
        val = struct.unpack('Q', self._conv(self.data[self.pos:pos2]))[0]
        self.pos = pos2
        return val

    def readRest(self):
        pos2 = len(self.data)
        val = self.data[self.pos:pos2]
        self.pos = pos2
        return val
