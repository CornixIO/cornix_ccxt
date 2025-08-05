from cornix_ccxt.pro.binance_abs import binance_abs
from cornix_ccxt.pro.exchange_spot import exchange_spot
from cornix_ccxt.strings import BINANCE


class binance_spot(exchange_spot, binance_abs):
    NAME = BINANCE
