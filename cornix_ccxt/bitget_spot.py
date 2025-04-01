from cornix_ccxt.bitget_abs import bitget_abs


class bitget_spot(bitget_abs):
    def __init__(self, config={}):
        super().__init__(config)
