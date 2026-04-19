from data.zones import zones

# -----------------------
# GET MAX VALUES
# -----------------------
def get_max_values():
    max_pop = max(z["population"] for z in zones.values())
    max_heat = max(z["heat"] for z in zones.values())
    return max_pop, max_heat


# -----------------------
# CALCULATE SCORE
# -----------------------
def calculate_score(zone, max_pop, max_heat):

    score = (
        0.35 * (1 - zone["ndvi"]) +                 # low greenery = high priority
        0.25 * (zone["population"] / max_pop) +     # more people = more impact
        0.20 * (zone["heat"] / max_heat) +          # heat stress
        0.20 * (zone["flood_risk"] / 10)            # flood vulnerability
    )

    return round(score * 100, 2)


# -----------------------
# APPLY SCORE TO ALL ZONES
# -----------------------
def apply_scores(zones):

    max_pop, max_heat = get_max_values()

    for zone_id, zone in zones.items():
        zone["score"] = calculate_score(zone, max_pop, max_heat)

        # Mandatory flag
        zone["mandatory"] = zone["ndvi"] < 0.15