from ccxt.pro.kucoin import kucoin

from cornix_ccxt.pro.exchange_spot import exchange_spot
from cornix_ccxt.strings import KUCOIN


class kucoin_spot(exchange_spot, kucoin):
    NAME = KUCOIN
