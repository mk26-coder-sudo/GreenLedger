from data.zones import zones
 #Find max values (for normalization)
def get_max_values():
    max_pop = max(z["population"] for z in zones.values())
    max_heat = max(z["heat"] for z in zones.values())
    return max_pop, max_heat
#Score function
def calculate_score(zone, max_pop, max_heat):
    score = (
        0.35 * (1 - zone["ndvi"]) +
        0.25 * (zone["population"] / max_pop) +
        0.20 * (zone["heat"] / max_heat) +
        0.20 * (zone["flood_risk"] / 10)
    )
    return round(score * 100, 2)