from ccxt.pro.bingx import bingx

from cornix_ccxt.pro.exchange_abs import exchange_abs


class bingx_abs(exchange_abs, bingx):
    COMMON_CURRENCIES = {
        'TONCOIN': 'TON',
    }
