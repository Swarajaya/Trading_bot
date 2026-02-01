import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        api_key=os.getenv("BINANCE_API_KEY"),
        api_secret=os.getenv("BINANCE_API_SECRET"),
        testnet=True
    )

    
    server_time = client.get_server_time()
    server_ts = server_time["serverTime"]
    local_ts = int(time.time() * 1000)

    client.timestamp_offset = server_ts - local_ts

    return client

