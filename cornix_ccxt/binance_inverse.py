from typing import Any

from ccxt.base.errors import PermissionDenied

from cornix_ccxt.binance_futures_abs import binance_futures_abs


class binance_inverse(binance_futures_abs):
    def describe(self) -> Any:
        return self.deep_extend(super(binance_inverse, self).describe(), {
            'options': {
                'fetchMarkets': ['inverse'],
                'defaultType': 'delivery',
                'defaultSubType': 'inverse',
            },
            'exceptions': {
                'inverse': {
                    'exact': {
                        '-4109': PermissionDenied,
                    }
                }
            }
        })
