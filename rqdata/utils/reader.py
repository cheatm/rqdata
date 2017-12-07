from fxdayu_data.handler.bundle import BLPTable
from datetime import datetime


class DITTable(BLPTable):

    def __init__(self, rootdir, index, dit):
        super(DITTable, self).__init__(rootdir, index)
        self.dit = dit

    def read(self, name, fields=None, start=None, end=None, length=None):
        if isinstance(start, datetime):
            start = self.dit.detrans(start)
        if isinstance(end, datetime):
            end = self.dit.detrans(end)

        return super(DITTable, self).read(name, fields, start, end, length)

    def _read(self, name, columns, start, end, length):
        return super(DITTable, self)._read(name, columns, start, end, length).rename_axis(self.dit.trans)
