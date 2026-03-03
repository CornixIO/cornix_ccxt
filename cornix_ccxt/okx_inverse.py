from typing import Any

from cornix_ccxt.okx_abs import okx_abs


class okx_inverse(okx_abs):
    def should_filter_balance_asset(self, code: str) -> bool:
        return code == 'USDT'

    def describe(self) -> Any:
        return self.deep_extend(super(okx_inverse, self).describe(), {
            'options': {
                'defaultType': 'inverse',
                'fetchMarkets': ['swap'],
            },
        })
