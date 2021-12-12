class Telescope:
    def __init__(self, isEquatorial = False, lookAt = [[0, 0], [0, 0]], destination = None):
        super(Telescope, self).__init__()

        self.isEquatorial = isEquatorial

        self.__class__.validateLookAt(lookAt)
        self.lookAt = lookAt
        self.initialLookAt = lookAt

        if destination is not None:
            self.__class__.validateLookAt(destination)
            self.destination = destination
        else:
            self.destination = self.initialLookAt

    def validateLookAt(lookAt):
        if len(lookAt) < 2:
            raise Exception('Invalid axes')

        if len(lookAt[0]) < 2:
            raise Exception('Invalid axe 0')

        if len(lookAt[1]) < 2:
            raise Exception('Invalid axe 1')

    def move(self, axisIdx, direction, amount):
        destination = self.initialLookAt if self.destination is None else self.destination
        destination[axisIdx][direction] += amount

        self.__class__.validateLookAt(destination)
        self.destination = destination

        print('moving to ' + str(self.destination) + '...')

        self.lookAt = self.destination