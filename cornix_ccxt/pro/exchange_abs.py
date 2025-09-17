from typing import Any, List

from ccxt.async_support.base.exchange import Exchange
from ccxt.base.types import Market


class exchange_abs(Exchange):
    NAME = ''
    FILTER_SYMBOL_TYPE = None
    DEFAULT_TYPE = None
    DEFAULT_SUBTYPE = None
    FETCH_MARGINS = None
    FETCH_MARKETS = None
    COMMON_CURRENCIES = None

    def __init__(self, config={}):
        super().__init__(config)
        self.options['defaultType'] = self.DEFAULT_TYPE
        if self.DEFAULT_SUBTYPE is not None:
            self.options['defaultSubType'] = self.DEFAULT_SUBTYPE
        if self.FETCH_MARGINS is not None:
            self.options['fetchMargins'] = self.FETCH_MARGINS
        if self.FETCH_MARKETS is not None:
            self.options['fetchMarkets'] = self.FETCH_MARKETS
        if self.COMMON_CURRENCIES is not None:
            self.options['commonCurrencies'] = self.COMMON_CURRENCIES

    async def fetch_markets(self, params={}) -> List[Market]:
        markets = await super().fetch_markets(params)
        markets_to_remove = []
        filter_type = self.DEFAULT_SUBTYPE or self.DEFAULT_TYPE
        for market in markets:
            if market['type'] != self.FILTER_SYMBOL_TYPE or not market[filter_type]:
                markets_to_remove.append(market)
            symbol = market['symbol']
            if ':' in symbol:
                symbol = symbol.split(':')[0]
                market['symbol'] = symbol
        for market in markets_to_remove:
            markets.remove(market)
        return markets
