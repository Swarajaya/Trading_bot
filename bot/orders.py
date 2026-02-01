import time

def place_market_order(client, symbol, side, quantity):
    return client.create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

def place_limit_order(client, symbol, side, quantity, price):
    return client.create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

def place_stop_limit_order(client, symbol, side, quantity, price, stop_price):
    return client.create_order(
        symbol=symbol,
        side=side,
        type="STOP_LOSS_LIMIT",
        quantity=quantity,
        price=price,
        stopPrice=stop_price,
        timeInForce="GTC"
    )

def place_oco_order(client, symbol, side, quantity, price, stop_price, limit_price):
    return client.create_oco_order(
        symbol=symbol,
        side=side,
        quantity=quantity,
        price=price,
        stopPrice=stop_price,
        stopLimitPrice=limit_price,
        stopLimitTimeInForce="GTC"
    )

def place_twap_order(client, symbol, side, quantity, slices, interval):
    qty_per_slice = quantity / slices
    orders = []

    for _ in range(slices):
        order = client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty_per_slice
        )
        orders.append(order)
        time.sleep(interval)

    return orders
