from typing import Any

from cornix_ccxt.pro.bybit_abs import bybit_abs


class bybit_inverse(bybit_abs):
    FILTER_SYMBOL_TYPE = 'swap'

    def describe(self) -> Any:
        return self.deep_extend(super().describe(), {
            'options': {
                'fetchMarkets': ['inverse'],
                'defaultType': 'delivery',
                'defaultSubType': 'inverse',
            },
        })
