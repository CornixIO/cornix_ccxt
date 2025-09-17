from ccxt.pro.kucoinfutures import kucoinfutures

from cornix_ccxt.pro.exchange_futures import exchange_futures
from cornix_ccxt.strings import KUCOIN_FUTURES


class kucoin_futures(exchange_futures, kucoinfutures):
    NAME = KUCOIN_FUTURES
