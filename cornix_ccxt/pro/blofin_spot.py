from cornix_ccxt.pro.blofin_abs import blofin_abs
from cornix_ccxt.pro.exchange_futures import exchange_futures
from cornix_ccxt.strings import BLOFIN_SPOT


class blofin_spot(exchange_futures, blofin_abs):
    NAME = BLOFIN_SPOT
