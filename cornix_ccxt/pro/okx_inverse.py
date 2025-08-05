from cornix_ccxt.pro.exchange_inverse import exchange_inverse
from cornix_ccxt.pro.okx_abs import okx_abs
from cornix_ccxt.strings import OKX_INVERSE


class okx_inverse(exchange_inverse, okx_abs):
    NAME = OKX_INVERSE
