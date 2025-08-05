from typing import Any

from cornix_ccxt.pro.binance_abs import binance_abs


class binance_spot(binance_abs):
    FILTER_SYMBOL_TYPE = 'spot'

    def describe(self) -> Any:
        return self.deep_extend(super().describe(), {
            'options': {
                'fetchMarkets': ['spot'],
                'fetchMargins': False,
                'defaultType': 'spot',
            },
        })
