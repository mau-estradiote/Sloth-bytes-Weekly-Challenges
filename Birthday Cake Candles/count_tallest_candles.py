def count_tallest_candles(candles):
    if not candles:
        return 0
    counts = {height: candles.count(height) for height in candles}
    return counts[max(candles)]