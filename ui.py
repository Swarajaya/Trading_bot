import streamlit as st

from bot.client import get_client
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
    place_twap_order,
)

st.set_page_config(page_title="Trading Bot UI", layout="centered")

st.title("📈 Trading Bot – Lightweight UI")

# --- Sidebar ---
st.sidebar.header("Order Settings")

symbol = st.sidebar.text_input("Symbol", value="BTCUSDT")
side = st.sidebar.selectbox("Side", ["BUY", "SELL"])
order_type = st.sidebar.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP_LIMIT", "TWAP"]
)

quantity = st.sidebar.number_input("Quantity", min_value=0.0, value=0.001, step=0.001)

price = st.sidebar.number_input("Price", min_value=0.0, value=90000.0, step=100.0)
stop_price = st.sidebar.number_input("Stop Price", min_value=0.0, value=88000.0, step=100.0)

interval = st.sidebar.number_input(
    "TWAP Interval (seconds)", min_value=1, value=5, step=1
)
slices = st.sidebar.number_input(
    "TWAP Slices", min_value=1, value=3, step=1
)

# --- Place Order ---
if st.button("🚀 Place Order"):
    try:
        client = get_client()

        if order_type == "MARKET":
            result = place_market_order(
                client, symbol, side, quantity
            )

        elif order_type == "LIMIT":
            result = place_limit_order(
                client, symbol, side, quantity, price
            )

        elif order_type == "STOP_LIMIT":
            result = place_stop_limit_order(
                client,
                symbol,
                side,
                quantity,
                price,
                stop_price
            )

        elif order_type == "TWAP":
            result = place_twap_order(
                client,
                symbol,
                side,
                quantity,
                interval,
                slices
            )

        st.success("✅ Order placed successfully")
        st.json(result)

    except Exception as e:
        st.error("❌ Error placing order")
        st.exception(e)
