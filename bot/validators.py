def validate_order(symbol, side, order_type, quantity, price=None):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type in ["LIMIT", "STOP_LIMIT"] and price is None:
        raise ValueError(f"{order_type} requires a price")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
