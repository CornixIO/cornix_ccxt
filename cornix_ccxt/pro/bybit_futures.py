from typing import Any, List



from cornix_ccxt.pro.bybit_abs import bybit_abs


class bybit_futures(bybit_abs):
    FILTER_SYMBOL_TYPE = 'swap'

    def describe(self) -> Any:
        return self.deep_extend(super().describe(), {
            'options': {
                'fetchMarkets': ['linear'],
                'defaultType': 'future',
                'defaultSubType': 'linear',
            },
        })
