from ccxt.coinbase import coinbase


class coinbase_advanced_spot(coinbase):
    def __init__(self, config={}):
        super().__init__(config)
