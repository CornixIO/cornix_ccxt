from cornix_ccxt.pro.exchange_abs import exchange_abs


class exchange_futures(exchange_abs):
    NAME = ''
    FILTER_SYMBOL_TYPE = 'swap'
    DEFAULT_TYPE = 'future'
    DEFAULT_SUBTYPE = 'linear'
    FETCH_MARKETS = ['linear']
