from cornix_ccxt.pro.exchange_abs import exchange_abs


class exchange_inverse(exchange_abs):
    NAME = ''
    FILTER_SYMBOL_TYPE = 'swap'
    DEFAULT_TYPE = 'delivery'
    DEFAULT_SUBTYPE = 'inverse'
    FETCH_MARKETS = ['inverse']
