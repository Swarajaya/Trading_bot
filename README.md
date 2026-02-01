Trading Bot (Binance Spot Testnet)

A Python-based trading bot with CLI + Lightweight UI, supporting multiple order types on Binance Spot Testnet.

This project was built as part of a Python Developer Intern assignment, focusing on correctness, clean structure, validation, and extensibility.

⚠️ Uses Binance Spot Testnet — no real funds are involved.

✨ Features
Core (Required)

Place MARKET orders

Place LIMIT orders

Binance Spot Testnet integration

Proper logging of all orders

Clean, modular project structure

CLI-based order execution

⭐ Bonus (All Implemented)

STOP-LIMIT order support

TWAP (Time-Weighted Average Price) execution

Lightweight Streamlit UI for interactive trading

📁 Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   ├── logging_config.py   # Logger setup
│
├── cli.py                  # CLI entry point
├── ui.py                   # Streamlit UI
├── trading.log             # Order logs (generated at runtime)
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone <your-repo-url>
cd trading_bot

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret


🔐 .env is intentionally excluded via .gitignore to prevent leaking API keys.

🖥️ CLI Usage
🔹 Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

🔹 Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000

🔹 Stop-Limit Order ✅
python cli.py --symbol BTCUSDT --side SELL --type STOP_LIMIT \
--quantity 0.001 --price 76000 --stop_price 77000

🔹 TWAP Order ✅
python cli.py --symbol BTCUSDT --side SELL --type TWAP \
--quantity 0.03 --interval 5 --slices 3

📌 Expected Behavior

Orders execute in multiple slices (TWAP)

Multiple API responses returned

All executions logged to trading.log

🌐 UI Usage (Optional Bonus)

Run the UI:

streamlit run ui.py

UI Supports

MARKET

LIMIT

STOP-LIMIT

TWAP

Live JSON response display

Validation with success/error feedback

📝 Logs

All orders are logged to:

trading.log


Logs include:

Order type

Status (NEW, FILLED)

Timestamp

Full Binance API response
