def score(result):
    profit = result["profit"]
    total = result["total"]

    profit_per_km = profit / total if total else 0

    if profit_per_km >= 0.18:
        recommendation = "ACCEPT"
        score = 90
    elif profit_per_km >= 0.15:
        recommendation = "NEGOTIATE"
        score = 70
    else:
        recommendation = "REJECT"
        score = 40

    result["profit_per_km"] = round(profit_per_km, 2)
    result["score"] = score
    result["recommendation"] = recommendation

    return result