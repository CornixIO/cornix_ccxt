from cornix_ccxt.pro.exchange_spot import exchange_spot
from cornix_ccxt.pro.okx_abs import okx_abs
from cornix_ccxt.strings import OKX


class okx_spot(exchange_spot, okx_abs):
    NAME = OKX
