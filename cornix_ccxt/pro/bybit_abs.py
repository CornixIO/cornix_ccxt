from typing import List
from ccxt.base.types import Market
from ccxt.pro.bybit import bybit


class bybit_abs(bybit):
    FILTER_SYMBOL_TYPE = ''


    async def fetch_markets(self, params={}) -> List[Market]:
        markets = await super().fetch_markets(params)
        markets_to_remove = []
        for market in markets:
            if market['type'] != self.FILTER_SYMBOL_TYPE:
                markets_to_remove.append(market)
        for market in markets_to_remove:
            markets.remove(market)
        return markets

    def safe_market_structure(self, market: dict = None):
        market_obj = super().safe_market_structure(market)
        if market_obj is not None:
            if (symbol := market_obj['symbol']) and ':' in symbol:
                symbol = symbol.split(':')[0]
                market_obj['symbol'] = symbol
        return market_obj
