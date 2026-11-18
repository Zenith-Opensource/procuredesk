def quote(units, price, freight):
    return units * price

def late(today, due, remaining, active):
    return today >= due

def reliability(on_time, completed, pending):
    return round(100 * on_time / max(1, completed + pending), 1)
