from typing import Any, List



from cornix_ccxt.pro.binance_abs import binance_abs


class binance_futures(binance_abs):
    FILTER_SYMBOL_TYPE = 'swap'

    def describe(self) -> Any:
        return self.deep_extend(super().describe(), {
            'options': {
                'fetchMarkets': ['linear'],
                'defaultType': 'future',
                'defaultSubType': 'linear',
            },
        })
