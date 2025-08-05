from typing import Any

from cornix_ccxt.pro.bybit_abs import bybit_abs


class bybit_spot(bybit_abs):
    FILTER_SYMBOL_TYPE = 'spot'

    def describe(self) -> Any:
        return self.deep_extend(super().describe(), {
            'options': {
                'fetchMarkets': ['spot'],
                'fetchMargins': False,
                'defaultType': 'spot',
            },
        })
