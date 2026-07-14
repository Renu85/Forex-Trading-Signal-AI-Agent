def generate_signal(row):

    score = 0

    if row["SMA20"] > row["SMA50"]:
        score += 1
    else:
        score -= 1

    if row["MACD"] > row["MACDSignal"]:
        score += 1
    else:
        score -= 1

    if row["RSI"] < 30:
        score += 1

    elif row["RSI"] > 70:
        score -= 1

    if score >= 2:
        return "BUY"

    elif score <= -2:
        return "SELL"

    return "HOLD"