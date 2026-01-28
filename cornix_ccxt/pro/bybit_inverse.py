from cornix_ccxt.pro.bybit_abs import bybit_abs
from cornix_ccxt.pro.exchange_inverse import exchange_inverse
from cornix_ccxt.strings import BYBIT


class bybit_inverse(exchange_inverse, bybit_abs):
    NAME = BYBIT
