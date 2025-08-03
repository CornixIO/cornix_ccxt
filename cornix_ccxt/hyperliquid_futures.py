from typing import List

from ccxt.base.types import Market
from cornix_ccxt.hyperliquid_abs import hyperliquid_abs


class hyperliquid_futures(hyperliquid_abs):
    def __init__(self, config={}):
        super().__init__(config)
        self.options['defaultType'] = 'swap'

    def fetch_markets(self, params={}) -> List[Market]:
        markets = self.fetch_swap_markets(params)
        for market in markets:
            market['symbol'] = market['symbol'].split(':')[0]
        markets = self.replace_k_with_1000(markets)
        return markets
