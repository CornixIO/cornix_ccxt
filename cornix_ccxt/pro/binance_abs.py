from typing import List
from ccxt.base.types import Market
from ccxt.pro.binance import binance


class binance_abs(binance):
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

    def parse_market(self, market: dict) -> Market:
        market_obj = super().parse_market(market)
        if market_obj is not None:
            symbol = market_obj['symbol']
            if ':' in symbol:
                symbol = symbol.split(':')[0]
                market_obj['symbol'] = symbol
        return market_obj
