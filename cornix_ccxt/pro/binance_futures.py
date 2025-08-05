from cornix_ccxt.pro.binance_abs import binance_abs
from cornix_ccxt.pro.exchange_futures import exchange_futures
from cornix_ccxt.strings import BINANCE_FUTURES


class binance_futures(exchange_futures, binance_abs):
    NAME = BINANCE_FUTURES
