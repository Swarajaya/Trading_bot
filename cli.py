import argparse
from bot.client import get_client
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
    place_oco_order,
    place_twap_order,
)
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser("Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True,
                        choices=["MARKET", "LIMIT", "STOP_LIMIT", "OCO", "TWAP"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)
    parser.add_argument("--limit_price", type=float)
    parser.add_argument("--interval", type=int, default=5)
    parser.add_argument("--slices", type=int, default=5)

    args = parser.parse_args()
    client = get_client()

    try:
        if args.type == "MARKET":
            order = place_market_order(client, args.symbol, args.side, args.quantity)

        elif args.type == "LIMIT":
            order = place_limit_order(
                client, args.symbol, args.side, args.quantity, args.price
            )

        elif args.type == "STOP_LIMIT":
            order = place_stop_limit_order(
                client, args.symbol, args.side,
                args.quantity, args.price, args.stop_price
            )

        elif args.type == "OCO":
            order = place_oco_order(
                client, args.symbol, args.side,
                args.quantity, args.price,
                args.stop_price, args.limit_price
            )

        elif args.type == "TWAP":
            order = place_twap_order(
                client, args.symbol, args.side,
                args.quantity, args.slices, args.interval
            )

        logger.info(f"Order success: {order}")
        print("✅ ORDER SUCCESS")
        print(order)

    except Exception as e:
        logger.error(f"Order failed: {e}")
        print("❌ ORDER FAILED")
        print(e)

if __name__ == "__main__":
    main()
