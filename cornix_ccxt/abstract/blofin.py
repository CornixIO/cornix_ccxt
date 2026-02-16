from ccxt.base.types import Entry


class ImplicitAPI:
    private_get_trade_order_detail = privateGetTradeOrderDetail = Entry('trade/order-detail', 'private', 'GET', {'cost': 1})
    private_get_trade_order_tpsl_detail = privateGetTradeOrderTpslDetail = Entry('trade/order-tpsl-detail', 'private', 'GET', {'cost': 1})
