from cornix_ccxt.bitget import bitget


class bitget_abs(bitget):
    def __init__(self, config={}):
        super().__init__(config)
        self.headers['locale'] = 'en-US'
