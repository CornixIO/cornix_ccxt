from typing import List

from ccxt.base.types import Market

from cornix_ccxt.bingx_abs import bingx_abs


class bingx_spot(bingx_abs):
    def __init__(self, config={}):
        super().__init__(config)
        self.options['defaultType'] = 'spot'

    def fetch_markets(self, params={}) -> List[Market]:
        return self.fetch_spot_markets(params)
