# Simple rule-based species recommendation

SPECIES_TABLE = {
    "extreme": {"Neem": 60, "Peepal": 30, "Banyan": 10},
    "high": {"Neem": 50, "Peepal": 30, "Jamun": 20},
    "moderate": {"Jamun": 40, "Tamarind": 40, "Karanj": 20},
    "low": {"Mango": 40, "Guava": 30, "Neem": 30}
}


def get_heat_class(heat):
    if heat >= 4.5:
        return "extreme"
    elif heat >= 3.5:
        return "high"
    elif heat >= 2.5:
        return "moderate"
    else:
        return "low"


def get_species_mix(zone, total_saplings):

    heat_class = get_heat_class(zone["heat"])
    percent_mix = SPECIES_TABLE.get(heat_class, {"Neem": 70, "Peepal": 30})

    actual_mix = {}

    remaining = total_saplings

    for i, (species, percent) in enumerate(percent_mix.items()):
        if i == len(percent_mix) - 1:
            actual_mix[species] = remaining
        else:
            count = int((percent / 100) * total_saplings)
            actual_mix[species] = count
            remaining -= count

    return actual_mix