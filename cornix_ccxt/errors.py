from ccxt.base.errors import (BaseError, ExchangeError, InvalidOrder,
                              RateLimitExceeded)


class TradesNotFound(InvalidOrder):
    pass


class OrderCancelled(InvalidOrder):
    """Raised when you are trying to fetch or cancel a non-existent order"""
    pass


class MaxStopAllowed(ExchangeError):
    """"Raised when an exchange server replies with an error in JSON"""
    pass

class PositionNotFound(ExchangeError):
    pass


class NotChanged(BaseError):
    pass


class AccountRateLimitExceeded(RateLimitExceeded):
    pass
