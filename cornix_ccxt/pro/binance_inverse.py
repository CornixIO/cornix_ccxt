from typing import Any

from cornix_ccxt.pro.binance_abs import binance_abs
from cornix_ccxt.pro.exchange_inverse import exchange_inverse
from cornix_ccxt.strings import BINANCE_COINS


class binance_inverse(exchange_inverse, binance_abs):
    NAME = BINANCE_COINS
