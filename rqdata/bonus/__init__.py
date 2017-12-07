from rqdata.env import BUNDLE_ROOT, HOME
import os


EX_CUM = os.path.join(BUNDLE_ROOT, "ex_cum_factor.bcolz")
DIVIDENDS = os.path.join(BUNDLE_ROOT, "original_dividends.bcolz")
SPLIT = os.path.join(BUNDLE_ROOT, "split_factor.bcolz")

STOCKS_FILE = os.path.join(HOME, "stocks.json")


def get_stocks():
    import json

    return json.load(open(STOCKS_FILE)).get("stocks", [])
