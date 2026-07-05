from config import FUEL_PRICE, FUEL_ECONOMY

def calculate(fare, pickup, trip):
    total = pickup + trip

    fuel_used = total / FUEL_ECONOMY
    fuel_cost = fuel_used * FUEL_PRICE
    profit = fare - fuel_cost

    return {
        "fare": round(fare, 2),
        "pickup": round(pickup, 2),
        "trip": round(trip, 2),
        "total": round(total, 2),
        "fuel_used": round(fuel_used, 2),
        "fuel_cost": round(fuel_cost, 2),
        "profit": round(profit, 2)
    }