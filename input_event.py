from stream_reader import StreamReader

class InputEvent:
	def __init__(self):
		super(InputEvent, self).__init__()

	def parse(data):
		event = InputEvent()
		reader = StreamReader(data)
		reader.readInt16()
		event.time_sec = reader.readInt32()
		event.time_usec = reader.readInt32()
		event.type = reader.readUint8()
		event.code = reader.readUint8()
		event.value = reader.readRest()

		return event

	def __str__(self):
		return self.__class__.__name__ + ':' + "\n" \
			+ "\t" + 'time_sec: ' + str(self.time_sec) + "\n" \
			+ "\t" + 'time_usec: ' + str(self.time_usec) + "\n" \
			+ "\t" + 'type: ' + str(self.type) + "\n" \
			+ "\t" + 'code: ' + str(self.code) + "\n" \
			+ "\t" + 'value: ' + str(self.value) + "\n"
