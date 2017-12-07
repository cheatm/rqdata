from rqdata.bonus.reader import DatetimeTable, DividendTable
from fxdayu_data.handler.mongo_handler import update
from rqdata.bonus import EX_CUM, DIVIDENDS, SPLIT, get_stocks
from datetime import timedelta
from fxdayu_data import DataAPI
import logging


DAY = timedelta(days=1)


def update_bonus(code, collection, ex_cum, dividends, split):
    last = DataAPI.bonus(code, length=1)
    if len(last):
        date = last.index[-1]
        regular_update(code, date+DAY, collection, ex_cum, dividends, split)
    else:
        insert_all(code, collection, ex_cum, dividends, split)


def regular_update(code, date, collection, *tables):
    for table in tables:
        name = getattr(table, "NAME", None)
        data = table.read(code, start=date)
        if len(data):
            try:
                result = update(collection, data, index="ex_date")
            except Exception as e:
                logging.error("%s | %s | %s", code, name, e)
            else:
                logging.warning("%s | %s | %s", code, name, result.upserted_count)


def insert_all(code, collection, *tables):
    collection.create_index("datetime", unique=True, background=True)
    for table in tables:
        name = getattr(table, "NAME", None)
        data = table.read(code)
        if len(data):
            try:
                result = update(collection, data, index="ex_date")
            except Exception as e:
                logging.error("%s | %s | %s", code, name, e)
            else:
                logging.warning("%s | %s | %s", code, name, result.upserted_count)


def updates(codes=None):
    if codes is None:
        codes = get_stocks()
    elif isinstance(codes, str):
        codes = codes.split(",")

    logging.warning("start")

    if len(codes) < 1:
        logging.error("Length of codes should be > 1, but input codes are %s", codes)
        return

    db = DataAPI.bonus.reader.db

    ex_cum = DatetimeTable(EX_CUM, "start_date")
    ex_cum.NAME = "ex_cum_factor"
    split = DatetimeTable(SPLIT, "ex_date")
    split.NAME = "split_factor"
    dividends = DividendTable(DIVIDENDS, "ex_date")
    dividends.NAME = "original_dividends"

    for code in codes:
        update_bonus(code, db[code], ex_cum, dividends, split)

    logging.warning("end")


if __name__ == '__main__':
    updates()


