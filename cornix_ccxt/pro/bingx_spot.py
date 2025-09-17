from cornix_ccxt.pro.bingx_abs import bingx_abs
from cornix_ccxt.pro.exchange_futures import exchange_futures
from cornix_ccxt.strings import BINGX_SPOT


class bingx_spot(exchange_futures, bingx_abs):
    NAME = BINGX_SPOT
