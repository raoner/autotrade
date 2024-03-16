import os
from dotenv import load_dotenv
load_dotenv()
import pyupbit
import pandas as pd
import pandas_ta as ta
import json
from openai import OpenAI
import schedule
import time

# Setup
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))


result = pyupbit.get_orderbook(ticker="KRW-BTC")

df_daily = pyupbit.get_ohlcv("KRW-BTC", "day", count=30)
df_hourly = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=24)

print(df_daily)