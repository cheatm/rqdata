from fxdayu_data.tools.convert import IntTime


class DeIntTime(IntTime):

    def __init__(self, start, *mod):
        super(DeIntTime, self).__init__(start, *mod)
        self.factor = list(reversed(self.d))

    def detrans(self, dt):
        return sum(map(self._mul, dt.timetuple(), self.factor))

    @staticmethod
    def _mul(a, b):
        return a * b