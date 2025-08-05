from cornix_ccxt.pro.exchange_futures import exchange_futures
from cornix_ccxt.pro.okx_abs import okx_abs
from cornix_ccxt.strings import OKX_FUTURES


class okx_futures(exchange_futures, okx_abs):
    NAME = OKX_FUTURES
