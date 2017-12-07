from rqdata.utils.convert import DeIntTime
from rqdata.utils.reader import DITTable


class DatetimeTable(DITTable):

    def __init__(self, rootdir, index):
        super(DatetimeTable, self).__init__(rootdir, index, DeIntTime(1, 100, 100, 100, 100, 100, 10000))


class DividendTable(DITTable):

    def __init__(self, rootdir, index):
        super(DividendTable, self).__init__(rootdir, index, DeIntTime(1, 100, 100, 10000))

    def _read(self, name, columns, start, end, length):
        data = super(DividendTable, self)._read(name, columns, start, end, length)
        DATE_COLS = ["announcement_date", "closure_date", "payable_date"]
        data[DATE_COLS] = data[DATE_COLS].applymap(self.dit.trans)
        data["cash_before_tax"] *= 0.0001
        return data


