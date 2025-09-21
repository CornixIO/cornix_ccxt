from cornix_ccxt.pro.bybit_abs import bybit_abs
from cornix_ccxt.pro.exchange_futures import exchange_futures
from cornix_ccxt.strings import BYBIT_USDT


class bybit_futures(exchange_futures, bybit_abs):
    NAME = BYBIT_USDT
