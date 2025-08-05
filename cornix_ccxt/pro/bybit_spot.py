from cornix_ccxt.pro.bybit_abs import bybit_abs
from cornix_ccxt.pro.exchange_spot import exchange_spot
from cornix_ccxt.strings import BYBIT_SPOT


class bybit_spot(exchange_spot, bybit_abs):
    NAME = BYBIT_SPOT
