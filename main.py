import struct

from usb import core

from input_event import InputEvent

dev = core.find(idVendor=0x0e6f, idProduct=0x02d7)

print(str(dev))
print('----')

dev.set_configuration()

cfg = dev.configurations()[0]

print(str(cfg))
print('----')

itf = cfg.interfaces()[0]

print(str(itf))
print('----')

endpoint = itf.endpoints()[0]

print(str(endpoint))
print('----')

while True:
	msg = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, 1000)
	print(str(msg))

	event = InputEvent.parse(msg)

	print(str(event))
