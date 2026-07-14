import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands

def create_indicators(df):

    df["Return"] = df["Close"].pct_change()

    df["SMA20"] = df["Close"].rolling(20).mean()

    df["SMA50"] = df["Close"].rolling(50).mean()

    df["EMA20"] = df["Close"].ewm(span=20).mean()

    df["EMA50"] = df["Close"].ewm(span=50).mean()

    df["RSI"] = RSIIndicator(df["Close"]).rsi()

    macd = MACD(df["Close"])

    df["MACD"] = macd.macd()

    df["MACDSignal"] = macd.macd_signal()

    bb = BollingerBands(df["Close"])

    df["BBUpper"] = bb.bollinger_hband()

    df["BBLower"] = bb.bollinger_lband()

    return df