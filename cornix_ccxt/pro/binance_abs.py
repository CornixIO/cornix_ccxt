from ccxt.pro.binance import binance

from cornix_ccxt.pro.exchange_abs import exchange_abs


class binance_abs(exchange_abs, binance):
    def __init__(self, config={}):
        super().__init__(config)
        self.options['watchTrades'] = {'name': 'aggTrade'}
        self.options['watchTradesForSymbols'] = {'name': 'aggTrade'}
