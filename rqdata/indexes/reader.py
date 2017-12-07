from rqdata.utils.reader import DITTable, BLPTable
from rqdata.utils.convert import DeIntTime
from rqdata.indexes import index_root


PRICE = ["close", "high", "low", "open"]


def day_end(dt):
    return dt.replace(hour=15)


class IndexTable(DITTable):

    def __init__(self, rootdir):
        super(IndexTable, self).__init__(rootdir, "date", DeIntTime(1, 100, 100, 10000))

    def _read(self, name, columns, start, end, length):
        data = super(IndexTable, self)._read(name, columns, start, end, length).rename_axis(day_end)
        data[PRICE] = (data[PRICE]*0.0001).round(2)
        return data
