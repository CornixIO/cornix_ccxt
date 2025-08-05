from typing import Any

from cornix_ccxt.pro.binance_abs import binance_abs


class binance_inverse(binance_abs):
    FILTER_SYMBOL_TYPE = 'swap'

    def describe(self) -> Any:
        return self.deep_extend(super().describe(), {
            'options': {
                'fetchMarkets': ['inverse'],
                'defaultType': 'delivery',
                'defaultSubType': 'inverse',
            },
        })
