from ccxt.bitget import bitget


class bitget_spot(bitget):
    def __init__(self, config={}):
        super().__init__(config)
