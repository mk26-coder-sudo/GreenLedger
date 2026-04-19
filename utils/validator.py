def validate_zones(zones):
    required_keys = ["name", "ndvi", "population", "heat", "flood_risk", "neighbors", "wind_out", "drain_to"]

    for zone_id, data in zones.items():
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Zone {zone_id} missing key: {key}")