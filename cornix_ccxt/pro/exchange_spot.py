from cornix_ccxt.pro.exchange_abs import exchange_abs


class exchange_spot(exchange_abs):
    NAME = ''
    FILTER_SYMBOL_TYPE = 'spot'
    DEFAULT_TYPE = 'spot'
    FETCH_MARGINS = False
    FETCH_MARKETS = ['spot']
